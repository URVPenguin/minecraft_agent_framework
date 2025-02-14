from core.di.decorators.dependency import dependency
from core.di.decorators.inject import inject
from core.di.injectable import Injectable
from core.events.chat_event_adapter import ChatEventAdapter
from core.events.comand_event import CommandEvent
from core.events.event_dispatcher import EventDispatcher
from core.services.minecraft_service import MinecraftService
from functools import reduce
import sys

def parse_command(input_string):
    """
    Detects the command (starts with @) and separates it from the arguments if there are any.

    Parameters
    ----------
    input_string : string

    Returns
    -------
    command, arguments : string
    """
    parts = input_string.split()
    command = parts[0] if parts and parts[0].startswith('@') else None
    arguments = parts[1:] if len(parts) > 1 else []
    return command, arguments


def parse_arguments(arguments):
    """
    Parses arguments into args, kwargs format

    Parameters
    ----------
    arguments : string

    Returns
    -------
    arguments
        Returns args, kwargs
    """
    return reduce(
        lambda acc, arg: (
            (acc[0], {**acc[1], **{arg.split('=')[0]: arg.split('=')[1]}})
            if '=' in arg else (acc[0] + [arg], acc[1])
        ),
        arguments,
        ([], {})
    )

@dependency
class CommandService(Injectable):
    """
    Service to process commands entered by users, and to launch an event if it is a valid command.
    """
    _ms: MinecraftService = inject(MinecraftService)
    _dispatcher: EventDispatcher = inject(EventDispatcher)

    def __init__(self):
        super().__init__()

    def process_command(self, event: ChatEventAdapter):
        """
        Given a string, it determines if it is a command and if it is, it raises an event with it, so that listeners can act according to the event.

        Parameters
        ----------
        event : ChatEventAdapter

        Returns
        -------
        command : bool
            Indicates whether the processed command was a command or not.
        """
        command, arguments = parse_command(event.get_data())
        args, kwargs = parse_arguments(arguments)

        if command is not None:
            if command == "@exit":
                self._ms.close()
                sys.exit()

            self._dispatcher.dispatch(CommandEvent(event.get_entity_id(), command,args, kwargs))

        return command is not None