import pandas as pd
from time import sleep
from shell.docs import MERGE_LEFT

Command = list[str]

dataframes = {

}

def exit(_:Command):
    for mark in ['.','..','...']:
        print(mark)
        sleep(.5)
    quit()

def help(arguments:Command):
    print(arguments)
    if arguments[0] == 'merge':
        print(MERGE_LEFT)

def import_file(arguments:Command):
    alias = arguments[0]
    path = arguments[1]
    df = pd.read_csv(path,dtype=str) #TODO: I set the dtype as str in order to match numeric values in the filter_print function.
    dataframes[alias] = df

def merge_left(arguments:Command):
    if len(arguments) < 5:
        raise ValueError
    file1,file2,left_on,right_on,alias = arguments[0:5]
    if len(arguments) > 5:
        cols = arguments[5:]
        cols.append(right_on)
    else:
        cols = list(dataframes[file2].columns.values)
        print(cols)

    suffixes = (None,'_duplicate')

    file = pd.merge(dataframes[file1],dataframes[file2][cols],how='left',left_on=left_on,right_on=right_on,suffixes=suffixes)
    
    drop_cols = [col for col in file.columns if col.endswith("_duplicate")]
    file.drop(columns=drop_cols, inplace=True)
    print(file)
    dataframes[alias] = file

def show_files(_:Command):
    if len(dataframes) == 0:
        print("No files currently stored.")
    else:   
        print("Files presently stored:")
        for file in dataframes:
            print(f'Alias: {file}')

def show_cols(arguments:Command):
    alias = arguments[0]
    df = dataframes[alias]
    print(df.columns.values)

def show_data(arguments:Command):
    alias = arguments[0]
    if len(arguments) > 1:
        head =  int(arguments[1])
        print(dataframes[alias].head(head))
    else:
        print(dataframes[alias])
    
def filter_print(arguments:Command):
    alias = arguments[0]
    df = dataframes[alias]
    for i in range(1, len(arguments[1:]), 2):
        df = df.loc[df[arguments[i]]==arguments[i+1]]
    print(df)

def drop_file(arguments:Command):
    print('before')
    print(dataframes)

    alias = arguments[0]
    if alias in dataframes:
        dataframes.pop(alias)
    print('after')
    print(dataframes)