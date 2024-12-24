import pandas as pd
from commands.validations import validate_file_ext, validate_path_exists
from events import raise_event

from .model import Model


def import_xl(model: Model, alias: str, path: str, sheet: int | None = None) -> None:
    '''This is a helper note'''
    validate_path_exists(path)
    validate_file_ext(path, '.xlsx')

    df = pd.read_excel(path, sheet_name=sheet)
    if isinstance(df, dict):
        for k, v in df.items():
            k = k.replace(' ', '_')
            model.create(f'{alias}_{k}', v)
    else:
        model.create(alias, df)
    raise_event("import", "Imported!")
