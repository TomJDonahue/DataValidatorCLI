from src.commands.command_base import CommandArgs,Command
from time import sleep

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.
class ExitCommandArgs(CommandArgs):

    def __repr__(self) -> str:
        return f'Merge Command Args: None'


class ExitCommand(Command):

    def execute(self,_: ExitCommandArgs): #type: ignore #TODO: Let's see if this works
        for mark in ['.', '..', '...']:
            print(mark)
            sleep(.5)
        quit()