import pandas as pd
from time import sleep


dataframes = {

}

def exit(_:list[str]):
    for mark in ['.','..','...']:
        print(mark)
        sleep(.5)
    quit()

def import_file(arguments:list[str]):
    alias = arguments[0]
    path = arguments[1]
    df = pd.read_csv(path)
    dataframes[alias] = df

def merge_left(arguments:list[str]):
    file1,file2,on,alias = arguments[0:4]
    if len(arguments) > 4:
        cols = arguments[4:]
        cols.append(on)
    else:
        cols = list(dataframes[file2].columns.values)
        print(cols)

    suffixes = (None,'_duplicate')

    file = pd.merge(dataframes[file1],dataframes[file2][cols],how='left',on=on,suffixes=suffixes)
    
    cols = [col for col in file.columns if col.endswith("_duplicate")]
    file.drop(columns=cols, inplace=True)
    print(file)
    dataframes[alias] = file

def show_files(_:list[str]):
    if len(dataframes) == 0:
        print("No files currently stored.")
    else:   
        print("Files presently stored:")
        for file in dataframes:
            print(f'Alias: {file}')

def show_cols(arguments:list[str]):
    alias = arguments[0]
    df = dataframes[alias]
    print(df.columns.values)

def filter_print(arguments:list[str]):
    alias,col,condition = arguments
    df = dataframes[alias]
    # print(df[col])
    print(df.loc[df[col]==condition])
