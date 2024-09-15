import pandas as pd
from shell.commands import commands, ExitCommand,ImportCommand,MergeCommand,FilterPrintCommand,ShowColsCommand,ShowFilesCommand,ShowDataCommand,DropFileCommand

def parse_commands(commands:str) -> tuple[str, list[str]]:
    split_commands = commands.split()
    command = split_commands[0]
    arguments = [args for args in split_commands[1:] if args != '']
    print(f'Debug(parse_commands): Arguments: {arguments}')

    if arguments and arguments[0] == '-h':
        return 'help',[command]

    return command, arguments


def execute_command(command:str,args:list[str]):
    if command in commands:
        try:
            if commands[command].validate_args(args):
                commands[command].execute(args)
            else:
                print("Validation Failed")
        except ValueError:
            print("Incorrect Arguments Provided!")
        # except Exception:
        #     print(Exception)
        #     print("Error with command, please try again.")
        finally:
            print('')
    else:
        print("Command not recognized")
        print('')

def run_shell():
    while True:
        user_input = input("tell me what you want ")
        if user_input == "T":
            quit()
        command, args = parse_commands(user_input)
        execute_command(command,args)
