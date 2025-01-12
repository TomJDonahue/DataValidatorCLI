from commands.validations import validate_alias_exists
from events import raise_event

from .model import Model


def drop_file(model: Model, alias: str) -> None:
    raise_event("drop", f"Drop file {alias}")
    raise_event("drop", model.get_table_names())
    validate_alias_exists(model, alias)

    raise_event("drop", f"Dropping {alias}")
    model.delete(alias)
    raise_event("drop", f"Remaining files: {model.get_table_names()}")
