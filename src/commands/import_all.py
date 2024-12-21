from .model import Model
from .validations import validate_path_exists
from events import raise_event

from glob import glob
from os import path, getcwd
import pandas as pd


def import_all(model: Model, file_path: str | None = None) -> None:

    exts = ['*.csv', '*.xlsx']
    if file_path == None:
        file_path = getcwd()

    validate_path_exists(file_path)

    files = [f.split("/")[-1]
             for ext in exts for f in glob(path.join(file_path, ext))]

    file_msg = ""
    for file in files:
        try:
            alias = file.split(".")[0]
            model.create(alias, pd.read_csv(file))
            file_msg += f"\n - {file} imported as {alias}"
        except:
            pass

    raise_event("import_all", f"Import Results: {file_msg}")
