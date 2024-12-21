from .model import Model
from .validations import validate_alias_exists
from events import raise_event


def rename_file(model: Model, alias: str, new_alias: str) -> None:
    validate_alias_exists(model, alias)

    model.create(new_alias, model.read(alias))
    model.delete(alias)
    message = f"{alias} renamed to {new_alias}"
    raise_event("rename", message)
