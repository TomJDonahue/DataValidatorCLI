import pandas as pd
from shell.commands import exit,import_file,merge_left,show_files,show_cols,filter_print,show_data,help,drop_file

def parse_commands(commands:str) -> tuple[str, list[str]]:
    split_commands = commands.split()
    command = split_commands[0]
    arguments = [args for args in split_commands[1:] if args != '']
    print(f'Debug(parse_commands): Arguments: {arguments}')

    if arguments and arguments[0] == '-h':
        return 'help',[command]

    return command, arguments


commands = {
    'merge': merge_left,
    'exit': exit,
    'import':import_file,
    'files': show_files,
    'cols': show_cols,
    'filter_print': filter_print,
    'data': show_data,
    'help':help,
    'drop':drop_file
}

def execute_command(command:str,args:list[str]):
    if command in commands:
        try:
            commands[command](args)
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

        command, args = parse_commands(user_input)
        execute_command(command,args)
