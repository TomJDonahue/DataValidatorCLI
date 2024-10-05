from src.model.model import Model
from src.commands.validations import value_exists_in_dataframes
from src.commands.command_base import CommandArgs, Command
from pydantic.dataclasses import dataclass
from pydantic import model_validator,field_validator
from sys import maxsize

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.

@dataclass
class ShowDataCommandArgs(CommandArgs):

    model:Model
    alias: str
    # TODO: I have a bug here with this
    num: int = -1

    @model_validator(mode='after' )
    def validate_data_exists(self):
        if not value_exists_in_dataframes(self.model,self.alias):
            raise Exception(f"File {self.alias} not in dataframes")
        return self
    
    @field_validator('num')
    def validate_num(cls,value):
        if value == -1:
            value = maxsize
        return value

    def __repr__(self) -> str:
        return f'Drop File Command Args: \nalias: {self.alias}'


class ShowDataCommand(Command):

    def execute(self, args: ShowDataCommandArgs):  # type: ignore
        print(args.model.read(args.alias,args.num))
