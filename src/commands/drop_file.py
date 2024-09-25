from src.data.dictionary import dataframes
from src.commands.command_base import CommandArgs, Command

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.


class DropFileCommandArgs(CommandArgs):

    def __init__(self, alias) -> None:
        self.alias = alias

    @ property
    def alias(self):
        return self._alias

    @ alias.setter
    def alias(self, value):
        if value not in dataframes:
            raise Exception(f"File {value} not in dataframes")
        self._alias = value

    def __repr__(self) -> str:
        return f'Drop File Command Args: \nalias: {self.alias}'


class DropFileCommand(Command):

    def execute(self, args: DropFileCommandArgs):  # type: ignore
        print('before')
        print(dataframes)

        del dataframes[args.alias]
        print('after')
        print(dataframes)
