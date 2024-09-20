from src.data.dictionary import dataframes


def values_are_strings(*args) -> bool:
    for value in args:
        if not isinstance(value, str):
            return False
    return True


def value_exists_in_dataframes(arg: str) -> bool:
    return arg in dataframes


def cols_exists_in_dataframe(*args) -> bool:
    cols = dataframes[str(args[0])].columns.values.tolist()
    for arg in args[1:]:
        if arg not in cols:
            return False
    return True


def values_are_numereic(*args) -> bool:
    for value in args:
        if not value.isnumeric():
            return False
    return True
