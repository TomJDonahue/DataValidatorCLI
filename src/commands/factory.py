from typing import TypedDict,Type
from src.commands.command_base import Command, CommandArgs
from src.commands.merge import MergeCommand, MergeCommandArgs


FactoryResult = TypedDict('FactoryResult', {'command':Type[Command],'args':Type[CommandArgs]})

COMMANDS: dict[str,FactoryResult] = {
    "merge": {'command':MergeCommand,'args':MergeCommandArgs},
    "_": {"command":Command,"args":MergeCommandArgs}
}

# class FactoryResult(TypedDict):
#     command:Command
#     args:CommandArgs

result = {
    'merge': MergeCommand
}


# movie: Movie = {'name': 'Blade Runner', 'year': 1982}



def generate_cmd_and_args(cmd_str: str,args: list[str]) -> tuple[Command,CommandArgs]:
    if cmd_str not in COMMANDS:
        raise Exception(f"Command {cmd_str} does not exist.")
    _command = COMMANDS[cmd_str]['command']()
    _args = COMMANDS[cmd_str]['args'](*args)
    return _command, _args