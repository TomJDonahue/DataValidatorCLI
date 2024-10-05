from src.model.model import Model
import pandas as pd
from src.commands.command_base import CommandArgs, Command
from pydantic import field_validator
from pydantic.dataclasses import dataclass
from src.commands.validations import path_exists

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.


@dataclass
class ImportCommandArgs(CommandArgs):

    model:Model
    alias: str
    path: str

    @field_validator('path')
    def validate_path(cls, value):
        if not path_exists(value):
            raise Exception(f"File not found at path: {value}")
        return value

    def __repr__(self) -> str:
        return f'Import Command Args: \nalias: {self.alias} \npath: {self.path}'


class ImportCommand(Command):

    def execute(self, args: ImportCommandArgs):  # type: ignore
        # TODO: I set the dtype as str in order to match numeric values in the filter_print function.
        df = pd.read_csv(args.path, dtype=str)
        args.model.create(args.alias,df)
        print("Imported!")
