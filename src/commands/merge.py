from src.commands.validations import value_exists_in_dataframes, cols_exists_in_dataframe
import pandas as pd
from src.data.dictionary import dataframes
from src.commands.command_base import CommandArgs,Command
from pydantic.dataclasses import dataclass
from pydantic import model_validator, field_validator
from dataclasses import field

# TODO: This module still makes some direct calls to the dataframes dictionary. I want to abstract away from that.
@dataclass
class MergeCommandArgs(CommandArgs):

    file1: str
    file2: str
    left_on: str
    right_on: str
    alias: str
    cols: list[str] = field(default_factory=list)

    @field_validator('file1', 'file2')
    def validate_file_exists(cls, value):
        if not value_exists_in_dataframes(value):
            raise Exception("Value not present in Dataframes collection")
        return value

    @model_validator(mode='after')
    def validate_cols_exist(self):
        # TODO: Work on this
        if not cols_exists_in_dataframe(self.file1, self.left_on):
            raise Exception(f"{self.file1} does not have column {self.left_on}")
        for col in [self.right_on,*self.cols]:
            if not cols_exists_in_dataframe(self.file2,col):
                raise Exception(f"{self.file2} does not have column {col}")
        return self

    @model_validator(mode='after')
    def set_cols(self):
        if len(self.cols) > 0:
            self.cols.append(self.right_on)
        else:
            self.cols = dataframes[self.file2].columns.values.tolist()
        return self

    def __repr__(self) -> str:
        return f'Merge Command Args: \nfile1: {self.file1} \nfile2: {self.file2} \nleft_on: {self.left_on} \nright_on: {self.right_on} \nalias: {self.alias} \ncols: {self.cols}'


class MergeCommand(Command):

    def execute(self,args: MergeCommandArgs): #type: ignore #TODO: Let's see if this works
        file1, file2, left_on, right_on, alias,cols = args.file1, args.file2, args.left_on, args.right_on, args.alias,args.cols

        suffixes = (None, '_duplicate')

        file = pd.merge(dataframes[file1], dataframes[file2][cols], how='left',
                        left_on=left_on, right_on=right_on, suffixes=suffixes)

        drop_cols = [col for col in file.columns if col.endswith("_duplicate")]
        file.drop(columns=drop_cols, inplace=True)
        print(file)
        dataframes[alias] = file

