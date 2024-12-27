import importlib
import yaml
from pathlib import Path
from core.di.decorators.dependency import dependency
from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.events.event_dispatcher import EventDispatcher


@dependency
class AgentLoaderService(Injectable):
    """
    Dynamically load agents (bots) into the framework
    """
    _dispatcher: EventDispatcher = inject(EventDispatcher)

    def __init__(self):
        super().__init__()
        self.agents = []

    def load_agents(self, file_path="src/config.yml"):
        """
        Loads a list of agents registered in a config.yml, and returns a list of all instances.

        Parameters
        ----------
        file_path : str, optional

        Returns
        -------
        agents : list
        """
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        config_path = base_dir / file_path

        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        for key, module_path in config["agents"].items():
            try:
                module = importlib.import_module(module_path)
                if hasattr(module, 'create_agent'):
                    self.agents.append(module.create_agent())
            except ModuleNotFoundError:
                print(f"Module {module_path} not found.")

        list(map(lambda agent: self._dispatcher.register(agent.event_handler, agent)
        if agent.event_handler is not None else None, self.agents))

        return self.agents
