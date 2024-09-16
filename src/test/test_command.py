import unittest
import pandas as pd
from shell.commands import ImportCommand, dataframes
from pandas.api.types import is_object_dtype

class ImportCommmandTest(unittest.TestCase):

    def test_args_are_strings(self):
        self.assertFalse(ImportCommand.validate_args([1,2,3])) # type: ignore
    
    def test_only_two_args_passed(self):
        self.assertFalse(ImportCommand.validate_args(['file1','file1.csv','file2']))
    
    def test_validator_returns_false_if_file_does_not_exist(self):
        self.assertFalse(ImportCommand.validate_args(['file1','no/such/file/exists.csv']))

    def test_file_imports_to_dataframe_dict(self):
        path = 'file1.csv'
        alias = 'file1'
        ImportCommand.execute([alias,path])
        self.assertIn(alias,dataframes)

    def test_file_data_exists_fully_in_dataframe_dict(self):
        path = 'file1.csv'
        alias = 'file1'
        ImportCommand.execute([alias,path])
        df = pd.read_csv(path,dtype='str')
        self.assertTrue(df.equals(dataframes[alias]))
    
    def test_file_data_imports_as_dtype_obj(self):
        path = 'file1.csv'
        alias = 'file1'
        ImportCommand.execute([alias,path])
        df = dataframes[alias]
        for idx in range(len(df.columns.to_list())):
            self.assertTrue(is_object_dtype(df.loc[idx]))
