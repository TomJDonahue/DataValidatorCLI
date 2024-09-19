from dataclasses import dataclass
from abc import ABC
from typing import Callable,Protocol,Any

Validations = Callable[[dict], bool]


'''Validations'''
def values_are_strings(args: dict) -> bool:
    for value in args.values():
        if not isinstance(value, str):
            return False
    return True


def values_are_numereic(args: dict) -> bool:
    for value in args.values():
        if not value.isnumeric():
            return False
    return True

'''Arguments  '''
class CommandArgs(Protocol):
    
    def compose_args(self,args):
        pass


class MergeCommandArgs:

    # File 1
    # File 2
    # Left On
    # Right On
    # Right Columns to merge into Left (Optional)
    def compose_args(self):
        pass

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
        print(self.args)


def main():
    validations: list[Validations] = [values_are_strings,
                                    values_are_numereic
                                    ]
    my_dict = {1: "2", 3: "f"}
    args = CommandArgs(my_dict)
    print(validate_all(validations,args.args))


if __name__ == '__main__':
    main()
