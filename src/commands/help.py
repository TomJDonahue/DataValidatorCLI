from .model import Model
from events import raise_event


def help(_: Model, cmd: str):
    from .factory import COMMANDS
    if cmd not in COMMANDS:
        raise ValueError(f"{cmd} is not a valid command.")
    msg = COMMANDS[cmd].__doc__
    if msg is None:
        msg = f"There is no help documentation for the {cmd} command"

    raise_event("help", msg)
