import pandas as pd
from shell.core import exit,import_file,merge_left,show_files,show_cols,filter_print

# dataframes['file1'] = pd.read_csv('file1.csv')
# dataframes['file2'] = pd.read_csv('file2.csv')

def parse_commands(commands:str):
    split_commands = commands.split()
    command = split_commands[0]
    arguments = [args for args in split_commands[1:] if args != '']
    print(f'Debug(parse_commands): Arguments: {arguments}')

    return command, arguments


commands = {
    'merge': merge_left,
    'exit': exit,
    'import':import_file,
    'files': show_files,
    'cols': show_cols,
    'filter_print': filter_print
}

while True:
    user_input = input("tell me what you want ")

    command, args = parse_commands(user_input)
    try:
        commands[command](args)
    except ValueError:
        print("Incorrect Arguments Provided!")
    # except Exception:
    #     print(Exception)
    #     print("Error with command, please try again.")
    finally:
        print('')

