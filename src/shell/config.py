from os import getcwd
from src.shell.commands import (ExitCommand,
                      ShowFilesCommand,
                      ShowColsCommand,
                      FilterPrintCommand,
                      ShowDataCommand,
                      HelpCommand,
                      DropFileCommand,
                      ImportCommand)
from src.commands.merge import MergeCommand

DEFAULT_DIRECTORY = getcwd()

commands = {
    'merge': MergeCommand,
    'exit': ExitCommand,
    'files': ShowFilesCommand,
    'cols': ShowColsCommand,
    'filter_print': FilterPrintCommand,
    'data': ShowDataCommand,
    'help': HelpCommand,
    'drop': DropFileCommand,
    'import': ImportCommand
}


'''
Command
    Validates
    Executes
    Help

Command Factory
    Arguments dataclass
    Return Command

'''
