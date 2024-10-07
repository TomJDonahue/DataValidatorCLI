from src.commands.command_base import CommandArgs, Command
from pydantic.dataclasses import dataclass

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.

@dataclass
class ShowFilesCommandArgs(CommandArgs):

    def __repr__(self) -> str:
        return f'Show Files Command Args: None'


class ShowFilesCommand(Command):

    def execute(self, args: ShowFilesCommandArgs):  # type: ignore
        table_names = args.model.get_table_names()
        if len(table_names) == 0:
            print("No files currently stored.")
            return
        
        print("Files presently stored:")
        for name in table_names:
            print(f'Alias: {name}')
