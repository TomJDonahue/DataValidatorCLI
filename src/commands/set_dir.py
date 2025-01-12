from events import raise_event
from settings import settings

from .model import Model


def set_dir(_: Model, path: str) -> None:
    settings['cwd'] = path
    raise_event("setdir", f"Changed path to {path}")
    print(settings['cwd'])
