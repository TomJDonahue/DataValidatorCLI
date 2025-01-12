import pandas as pd
from commands.validations import validate_file_ext, validate_path_exists
from events import raise_event

from .model import Model


def import_xl(model: Model, alias: str, path: str, sheet: int | None = None) -> None:
    '''

    The importxl command imports an Excel (.xlsx) file. By default it loads all
    sheets of the document, but an optional paremeter can be provided to import
    only a specified sheet

    command: importxl
    arguments:
        alias: The name of the file in the application. If multiple sheets are imported
                they will be named [alias]_[sheet_name]. Note that all spaces in the sheet name
                will be replaced with underscores ( _ ).
        path: The location of the file to be imported
        sheet: [Optional] The sheet number to import, as arranged in the Excel document.
                If no value is provided, the command will import all sheets.
    '''
    validate_path_exists(path)
    validate_file_ext(path, '.xlsx')

    df = pd.read_excel(path, sheet_name=sheet)
    msg = 'Imported: '
    if isinstance(df, dict):
        for k, v in df.items():
            k = k.replace(' ', '_')
            model.create(f'{alias}_{k}', v)
            msg += f'{alias}_{k}\n'
    else:
        model.create(alias, df)
        msg += alias

    raise_event("import", msg)
