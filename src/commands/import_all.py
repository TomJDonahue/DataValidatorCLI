from typing import Callable
from .model import Model
from .validations import validate_path_exists
from events import raise_event

from glob import glob
from os import path, getcwd
import pandas as pd


def import_all(model: Model, file_path: str | None = None) -> None:

    exts = {'*.csv': pd.read_csv,
            '*.xlsx': pd.read_excel,
            }

    if file_path == None:
        file_path = getcwd()

    validate_path_exists(file_path)

    files = [f.split("/")[-1]
             for ext in exts.keys() for f in glob(path.join(file_path, ext))]

    file_msg = ""
    for file in files:
        alias, ext = file.split(".")
        ext = "*." + ext
        if ext in exts:
            try:
                df = exts[ext](file)
                model.create(alias, df)
                file_msg += f"\n - {file} imported as {alias}"
            except ValueError as e:
                file_msg += f"\n - Failed to import {file} due to:\n   - {e}"

    raise_event("import_all", f"Import Results: {file_msg}")
