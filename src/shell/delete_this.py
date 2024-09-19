from dataclasses import dataclass
from abc import ABC
from typing import Callable

Validations = Callable[[dict], bool]


def values_are_strings(args: dict) -> bool:
    for value in args.values():
        if not isinstance(value, str):
            print("heyo!")
            return False
    return True


def values_are_numereic(args: dict) -> bool:
    for value in args.values():
        if not value.isnumeric():
            return False
    return True


class CommandArgs:

    def __init__(self, args: dict) -> None:
        self.args = args


class CommandValidator:
    # TODO: There is no reason this needs to be a class.
    # The validate method is agnostic, and all that needs to be built separately is the validations list based on the individual command
    validations: list[Validations] = [values_are_strings,
                                      values_are_numereic
                                      ]

    def validate(self, args: dict):
        valid = True
        for validation in self.validations:
            if valid == True:
                print(f'running {validation.__name__}')
                valid = validation(args)
            elif valid == False:
                break
        return valid


class TestClass:
    def __init__(self, args: CommandArgs) -> None:
        self.args = args
        print(self.args)


def main():
    my_dict = {1: "2", 3: 4}
    args = CommandArgs(my_dict)
    validator = CommandValidator()
    print(validator.validate(args.args))


if __name__ == '__main__':
    main()
