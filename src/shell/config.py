from os import getcwd
from commands import (MergeCommand,
                      ExitCommand,
                      ShowFilesCommand,
                      ShowColsCommand,
                      FilterPrintCommand,
                      ShowDataCommand,
                      HelpCommand,
                      DropFileCommand,
                      ImportCommand)

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
