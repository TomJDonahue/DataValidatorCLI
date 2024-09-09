import pandas as pd

dataframes = {

}

dataframes['file1'] = pd.read_csv('file1.csv')
dataframes['file2'] = pd.read_csv('file2.csv')



def parse_commands(commands:str):
    arguments = commands.split()
    command = arguments[0]
    arguments = [args for args in arguments[1:] if args != '']
    print(arguments)

    return command, arguments

def merge(arguments):
    file1,file2,how,on = arguments

    print(on)
    if how =='left':
        suffixes = (None,'_duplicate')
    else:
        suffixes = ('_duplicate',None)

    file = pd.merge(dataframes[file1],dataframes[file2],how=how,on=on,suffixes=suffixes)
    
    cols = [col for col in file.columns if col.endswith("_duplicate")]
    file.drop(columns=cols, inplace=True)
    print(file)




commands = {
    'merge': merge
}

input = input("tell me what you want ")

command, args = parse_commands(input)
commands[command](args)
