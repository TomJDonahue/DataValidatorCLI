from src.data.dictionary import dataframes
from src.commands.command_base import CommandArgs, Command

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.


class ShowDataCommandArgs(CommandArgs):

    def __init__(self, alias, num=None) -> None:
        self.alias = alias
        self.num = num

    @ property
    def alias(self):
        return self._alias

    @ alias.setter
    def alias(self, value):
        if value not in dataframes:
            raise Exception(f"File {value} not in dataframes")
        self._alias = value

    
    @ property
    def num(self):
        return self._num
    
    @ num.setter
    def num(self,value):
        if value == None:
            return
        if not value.isnumeric():
            raise Exception(f"Num {value} is not a number.")
        self._num = value

    def __repr__(self) -> str:
        return f'Drop File Command Args: \nalias: {self.alias}'


class ShowDataCommand(Command):

    def execute(self, args: ShowDataCommandArgs):  # type: ignore
        print('before')
        print(dataframes)

        del dataframes[args.alias]
        print('after')
        print(dataframes)
