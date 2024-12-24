from os.path import exists

from .model import Model


def validate_alias_exists(model: Model, alias: str) -> None:
    if alias not in model.get_table_names():
        raise ValueError(f"File {alias} not in dataframes")


def validate_cols_exist(model: Model, alias: str, cols: list[str]) -> None:
    file_cols = set(model.read(alias).columns)
    for col in cols:
        if col not in file_cols:
            raise ValueError(f"Column {col} not in dataframe {alias}")


def validate_path_exists(path: str) -> None:
    if not exists(path):
        raise ValueError(f"File not found at path: {path}")


def validate_file_ext(file_name: str, ext: str) -> None:
    if not file_name.split('.')[-1] == ext.split('.')[-1]:
        raise ValueError(f"{file_name} is not {ext} format")
