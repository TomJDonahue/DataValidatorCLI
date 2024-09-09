import pandas as pd

dataframes = {

}

dataframes['file1'] = pd.read_csv('file1.csv')
dataframes['file2'] = pd.read_csv('file2.csv')

def parse_commands(commands:str):
    split_commands = commands.split()
    command = split_commands[0]
    arguments = [args for args in split_commands[1:] if args != '']
    print(arguments)

    return command, arguments

def merge_left(arguments):
    file1,file2,on = arguments[0:3]
    if len(arguments) > 3:
        cols = arguments[3:]
        cols.append(on)
    else:
        cols = list(dataframes[file2].columns.values)

    suffixes = (None,'_duplicate')

    file = pd.merge(dataframes[file1],dataframes[file2][cols],how='left',on=on,suffixes=suffixes)
    
    cols = [col for col in file.columns if col.endswith("_duplicate")]
    file.drop(columns=cols, inplace=True)
    print(file)




commands = {
    'merge': merge_left
}

input = input("tell me what you want ")

command, args = parse_commands(input)
try:
    commands[command](args)
except ValueError:
    print("Incorrect Arguments Provided!")

