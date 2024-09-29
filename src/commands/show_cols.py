from src.data.dictionary import dataframes
from src.commands.command_base import CommandArgs, Command
from pydantic.dataclasses import dataclass
from pydantic import field_validator

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.

@dataclass
class ShowColsCommandArgs(CommandArgs):

    alias: str

    @field_validator('alias')
    def validate_data_exists(cls, value):
        if value not in dataframes:
            raise Exception(f"File {value} not in dataframes")
        return value

    def __repr__(self) -> str:
        return f'Show Cols Command Args: \nalias: {self.alias}'


class ShowColsCommand(Command):

    def execute(self, args: ShowColsCommandArgs):  # type: ignore
        print(dataframes[args.alias].columns.values)
