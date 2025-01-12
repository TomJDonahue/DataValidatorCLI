import pandas as pd
from commands.validations import validate_path_exists, validate_file_ext
from events import raise_event
from os import path as ospath
from settings import settings

from .model import Model


def import_csv(model: Model, alias: str, path: str) -> None:
    path = ospath.join(settings['cwd'], path)
    print(path)
    validate_path_exists(path)
    validate_file_ext(path, '.csv')

    df = pd.read_csv(path)
    model.create(alias, df)
    raise_event("import", f"Imported: {alias}")
