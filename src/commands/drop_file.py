from src.commands.validations import value_exists_in_dataframes
from src.commands.command_base import CommandArgs, Command
from pydantic.dataclasses import dataclass
from pydantic import model_validator
from src.model.model import Model

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.

@dataclass
class DropFileCommandArgs(CommandArgs):

    alias: str

    @model_validator(mode='after')
    def validate_data_exists(self):
        if not value_exists_in_dataframes(self.model,self.alias):
            raise Exception(f"File {self.alias} not in dataframes")
        return self
    
    def __repr__(self) -> str:
        return f'Drop File Command Args: \nalias: {self.alias}'


class DropFileCommand(Command):

    def execute(self, args: DropFileCommandArgs):  # type: ignore
        print('before')
        print(args.model.get_table_names())

        args.model.delete(args.alias)
        print('after')
        print(args.model.get_table_names())
