from dataclasses import dataclass
from abc import ABC
from typing import Callable, Protocol, Any
import pandas as pd


file = pd.read_csv("file1.csv")

datyframeys = {"file1": file,
               "file2": file}


'''Validations'''


'''Arguments  '''


def validate_all(validations: list[Validations], args: dict):
    for validation in validations:
        task = validation.__name__
        print(f'running {task}')
        if validation(args) == False:
            print(f'failed {task}\n')
            return False
        print(f'succeeded {task}\n')
    return True


class TestClass:
    def __init__(self, args: CommandArgs) -> None:
        self.args = args
