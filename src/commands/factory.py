from typing import TypedDict, Type
from src.commands.command_base import Command, CommandArgs
from src.commands.merge import MergeCommand, MergeCommandArgs
from src.commands.import_df import ImportCommand, ImportCommandArgs
from src.commands.exit import ExitCommand, ExitCommandArgs
from src.commands.show_files import ShowFilesCommand, ShowFilesCommandArgs
from src.commands.show_cols import ShowColsCommand, ShowColsCommandArgs
from src.commands.drop_file import DropFileCommand, DropFileCommandArgs


FactoryResult = TypedDict(
    'FactoryResult', {'command': Type[Command], 'args': Type[CommandArgs]})

COMMANDS: dict[str, FactoryResult] = {
    "merge": {'command': MergeCommand, 'args': MergeCommandArgs},
    "import": {'command': ImportCommand, 'args': ImportCommandArgs},
    "exit": {'command': ExitCommand, 'args': ExitCommandArgs},
    "files": {'command': ShowFilesCommand, 'args': ShowFilesCommandArgs},
    "cols": {'command': ShowColsCommand, 'args': ShowColsCommandArgs},
    "drop": {'command': DropFileCommand, 'args': DropFileCommandArgs},
    "_": {"command": Command, "args": CommandArgs}
}


def generate_cmd_and_args(cmd_str: str, args: list[str]) -> tuple[Command, CommandArgs]:
    if cmd_str not in COMMANDS:
        raise Exception(f"Command {cmd_str} does not exist.")
    _command = COMMANDS[cmd_str]['command']()
    _args = COMMANDS[cmd_str]['args'](*args)
    return _command, _args
