import pandas as pd
from time import sleep
import shell.docs as docs
from typing import Protocol
from os.path import isfile

class Command(Protocol):
    @staticmethod
    def validate_args(args:list[str]):
        ...
    
    @staticmethod
    def execute(args:list[str]):
        ...
    
    @staticmethod
    def help():
        ... 

class ExitCommand:
    @staticmethod
    def validate_args(_:list[str]):
        return True
    
    @staticmethod
    def execute(_:list[str]):
        for mark in ['.','..','...']:
            print(mark)
            sleep(.5)
        quit()
    
    @staticmethod
    def help():
        ... 

class ImportCommand:
    @staticmethod
    def validate_args(args:list[str]):
        # Confirm the correct number of arguments are passed
        if len(args) != 2:
            return False
        # Confirm all arguments passed are strings
        for arg in args:
            if isinstance(arg,str) == False:
                return False
        # Confirm the second arg is a file that exists in the path.
        if not isfile(args[1]):
            return False
        return True
        
    
    @staticmethod
    def execute(args:list[str]):
        alias = args[0]
        path = args[1]
        df = pd.read_csv(path,dtype=str) #TODO: I set the dtype as str in order to match numeric values in the filter_print function.
        dataframes[alias] = df
    
    @staticmethod
    def help():
        ... 

class MergeCommand:
    @staticmethod
    def validate_args(args:list[str]):
        # Confirm there are enough arguments provided
        if len(args) < 5:
            print('not enough args')
            return False
        # First argument should be the left file and it should exist in the dataframes dictionary
        if args[0] not in dataframes:
            print('file1 not in dataframes')
            return False
        # Second argument should be the right file and it should exist in the dataframes dictionary
        if args[1] not in dataframes:
            print('file2 not in dataframes')
            return False
        # Third argument should be the ID column in the left file and should exist
        if args[2] not in dataframes[args[0]].columns.values.tolist():
            print('left_on not in file1')
            return False
        # Fourth argument should be the ID column in the right file and should exist
        if args[3] not in dataframes[args[1]].columns.values.tolist():
            print('right_on not in file2')
            return False
        # If there are arguments after the 4th, they should all be columns that exist in the right file
        for arg in args[5:]:
            if arg not in dataframes[args[1]].columns.values.tolist():
                return False
        return True
    
    @staticmethod
    def execute(args:list[str]):
        file1,file2,left_on,right_on,alias = args[0:5]
        if len(args) > 5:
            cols = args[5:]
            cols.append(right_on)
        else:
            cols = dataframes[file2].columns.values.tolist()
            print(cols)

        suffixes = (None,'_duplicate')

        file = pd.merge(dataframes[file1],dataframes[file2][cols],how='left',left_on=left_on,right_on=right_on,suffixes=suffixes)
        
        drop_cols = [col for col in file.columns if col.endswith("_duplicate")]
        file.drop(columns=drop_cols, inplace=True)
        print(file)
        dataframes[alias] = file
    
    @staticmethod
    def help():
        print(docs.MERGE_LEFT)

class ShowFilesCommand:
    @staticmethod
    def validate_args(_:list[str]):
        # Confirm whether there are any files stored in the dataframes dictionary
        if len(dataframes) == 0:
            print("No files currently stored.")
            return False
        return True
    
    @staticmethod
    def execute(_:list[str]):
        print("Files presently stored:")
        for file in dataframes:
            print(f'Alias: {file}')
        
    @staticmethod
    def help():
        ... 

class FilterPrintCommand:
    @staticmethod
    def validate_args(args:list[str]):
        # Confirm the minimum number of arguments have been provided
        if len(args) < 3:
            return False
        # First arg should be the file alias and it should exist in the dataframes dictionary
        if args[0] not in dataframes:
            return False
        # Every other arg should be a column that exists in the dataframe
        cols = dataframes[args[0]].columns.tolist()
        for idx in range(1,len(args),2):
            if args[idx] not in cols:
                return False
        return True
    
    @staticmethod
    def execute(args:list[str]):
        alias = args[0]
        df = dataframes[alias]
        for i in range(1, len(args[1:]), 2):
            df = df.loc[df[args[i]]==args[i+1]]
        print(df)
    
    @staticmethod
    def help():
        ... 

class ShowColsCommand:
    @staticmethod
    def validate_args(args:list[str]):
        # Confirm the minimum number of required arguments are passed.
        if len(args) < 1:
            return False
        # Confirm the first arg is a file that exists in the dataframes dict
        if args[0] not in dataframes:
            return False
        return True
    
    @staticmethod
    def execute(args:list[str]):
        print(dataframes[args[0]].columns.values)
    
    @staticmethod
    def help():
        ... 

class ShowDataCommand:
    @staticmethod
    def validate_args(args:list[str]):
        # Confirm the minimum number of arguments are passed
        if len(args) < 1:
            return False
        # Confirm the file is present in the dataframes dict.
        if args[0] not in dataframes:
            return False
        # If a second argument is provided, confirm that it can be converted to a number
        if len(args) > 1 and not args[1].isnumeric():
            print('failed!')
            return False
        return True
    
    @staticmethod
    def execute(args:list[str]):
        alias = args[0]
        if len(args) > 1:
            head =  int(args[1])
            print(dataframes[alias].head(head))
        else:
            print(dataframes[alias])
    
    @staticmethod
    def help():
        ... 

class DropFileCommand:
    @staticmethod
    def validate_args(args:list[str]):
        # Confirm the minimum number of arguments are provided
        if len(args) < 1:
            return False
        # Confirm that the file exists in the dataframes
        if args[0] not in dataframes:
            return False
        return True
    
    
    @staticmethod
    def execute(args:list[str]):
        print('before')
        print(dataframes)

        dataframes.pop(args[0])
        print('after')
        print(dataframes)
    
    @staticmethod
    def help():
        ... 

class HelpCommand:
    @staticmethod
    def validate_args(args:list[str]):
        if args and args[0] not in commands:
            return False
        return True
    
    @staticmethod
    def execute(args:list[str]):
        if len(args) == 0:
            help()
            return
        commands[args[0]].help()

    @staticmethod
    def help():
        print("HELP!!!!!!!!")

dataframes = {

}

commands = {
    'merge': MergeCommand,
    'exit': ExitCommand,
    'files': ShowFilesCommand,
    'cols': ShowColsCommand,
    'filter_print': FilterPrintCommand,
    'data': ShowDataCommand,
    '--help':HelpCommand,
    'drop':DropFileCommand,
    'import': ImportCommand
}