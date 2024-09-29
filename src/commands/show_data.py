from src.data.dictionary import dataframes
from src.commands.command_base import CommandArgs, Command
from pydantic.dataclasses import dataclass
from pydantic import field_validator
from sys import maxsize

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.

@dataclass
class ShowDataCommandArgs(CommandArgs):

    alias: str
    num: int = -1

    @field_validator('alias' )
    def validate_data_exists(cls, value):
        if value not in dataframes:
            raise Exception(f"File {value} not in dataframes")
        return value
    
    @field_validator('num')
    def validate_num(cls,value):
        if value == -1:
            value = maxsize
        return value

    def __repr__(self) -> str:
        return f'Drop File Command Args: \nalias: {self.alias}'


class ShowDataCommand(Command):

    def execute(self, args: ShowDataCommandArgs):  # type: ignore
        print(dataframes[args.alias].head(args.num))
