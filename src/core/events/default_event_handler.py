from core.events.interfaces.event_handler import EventHandler

class DefaultEventHandler(EventHandler):
    def handle_block_event(self, event, agent):
        pass

    def handle_chat_event(self, event, agent):
        pass

    def handle_command_event(self, event, agent):
        command, args, kwargs = event.get_data().values()
        agent.handle_command(command, args, kwargs)