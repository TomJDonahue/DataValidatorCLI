from validations import value_exists_in_dataframes, cols_exists_in_dataframe
import pandas as pd
from src.data.dictionary import dataframes


class MergeCommandArgs:

    def __init__(self, file1, file2, left_on, right_on, *cols) -> None:
        pass
        self.file1 = file1
        self.file2 = file2
        self.left_on = left_on
        self.right_on = right_on
        if cols == None:
            self.cols = []
        else:
            self.cols = cols

    @ property
    def file1(self):
        return self._file1

    @ file1.setter
    def file1(self, value):
        if not value_exists_in_dataframes(value):
            raise Exception("Value not present in Dataframes collection")
        self._file1 = value

    @ property
    def file2(self):
        return self._file2

    @ file2.setter
    def file2(self, value):
        if not value_exists_in_dataframes(value):
            raise Exception("Value not present in Dataframes collection")
        self._file2 = value

    @ property
    def left_on(self):
        return self._left_on

    @ left_on.setter
    def left_on(self, value):
        if not cols_exists_in_dataframe(self.file1, value):
            raise Exception(f"Left_on value {
                            value} does not exist in {self.file1}")
        self._left_on = value

    @ property
    def right_on(self):
        return self._right_on

    @ right_on.setter
    def right_on(self, value):
        if not cols_exists_in_dataframe(self.file2, value):
            raise Exception(f"Right_on value {
                            value} does not exist in {self.file2}")
        self._right_on = value

    @ property
    def alias(self):
        return self._alias

    @ alias.setter
    def alias(self, value):
        self._alias = value

    @ property
    def cols(self):
        return self._cols

    @ cols.setter
    def cols(self, value):
        if not cols_exists_in_dataframe(self.file2, *value):
            raise Exception(f"One or more of the following 
                            {value} does not exist in {self.file2}")
        self._cols = value

    def __repr__(self) -> str:
        return f'Merge Command Args: \nfile1: {self.file1} \nfile2: {self.file2} \nleft_on: {self.left_on} \nright_on: {self.right_on} \ncols: {self.cols}'


class MergeCommand:

    @staticmethod
    def execute(args: MergeCommandArgs):
        file1, file2, left_on, right_on, alias = args.file1, args.file2, args.left_on, args.right_on, args.alias
        if len(args.cols) > 0:
            cols = args.cols
            cols.append(right_on)
        else:
            cols = dataframes[file2].columns.values.tolist()
            print(cols)

        suffixes = (None, '_duplicate')

        file = pd.merge(dataframes[file1], dataframes[file2][cols], how='left',
                        left_on=left_on, right_on=right_on, suffixes=suffixes)

        drop_cols = [col for col in file.columns if col.endswith("_duplicate")]
        file.drop(columns=drop_cols, inplace=True)
        print(file)
        dataframes[alias] = file

