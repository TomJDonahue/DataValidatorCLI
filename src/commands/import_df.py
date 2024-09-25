from os.path import exists
import pandas as pd
from src.data.dictionary import dataframes
from src.commands.command_base import CommandArgs, Command

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.


class ImportCommandArgs(CommandArgs):

    def __init__(self, alias, path) -> None:
        self.alias = alias
        self.path = path

    @ property
    def alias(self):
        return self._alias

    @ alias.setter
    def alias(self, value):
        self._alias = value

    @ property
    def path(self):
        return self._path

    @ path.setter
    def path(self, value):
        if not exists(value):
            raise Exception(f"File not found at path: {value}")
        self._path = value

    def __repr__(self) -> str:
        return f'Import Command Args: \nalias: {self.alias} \npath: {self.path}'


class ImportCommand(Command):

    def execute(self, args: ImportCommandArgs):  # type: ignore
        # TODO: I set the dtype as str in order to match numeric values in the filter_print function.
        dataframes[args.alias] = pd.read_csv(args.path, dtype=str)
        print("Imported!")
