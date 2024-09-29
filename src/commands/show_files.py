from src.data.dictionary import dataframes
from os.path import exists
import pandas as pd
from src.data.dictionary import dataframes
from src.commands.command_base import CommandArgs, Command
from pydantic.dataclasses import dataclass

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.

@dataclass
class ShowFilesCommandArgs(CommandArgs):

    def __repr__(self) -> str:
        return f'Show Files Command Args: None'


class ShowFilesCommand(Command):

    def execute(self, _: ShowFilesCommandArgs):  # type: ignore
        if len(dataframes) == 0:
            print("No files currently stored.")
            return
        
        print("Files presently stored:")
        for file in dataframes:
            print(f'Alias: {file}')
