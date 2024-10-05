from src.model.model import Model
from src.commands.command_base import CommandArgs,Command
from time import sleep
from pydantic.dataclasses import dataclass

@dataclass
class ExitCommandArgs(CommandArgs):

    model:Model
    def __repr__(self) -> str:
        return f'Merge Command Args: None'


class ExitCommand(Command):

    def execute(self,_: ExitCommandArgs): #type: ignore #TODO: Let's see if this works
        for mark in ['.', '..', '...']:
            print(mark)
            sleep(.5)
        quit()