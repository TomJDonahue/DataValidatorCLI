import inspect
from typing import Any, Callable


from .drop_file import drop_file
from .exit import exit_app
from .import_csv import import_csv
from .merge import merge
from .show_cols import show_cols
from .show_data import show_data
from .show_files import show_files
from .rename_file import rename_file
from .import_all import import_all
from .import_xl import import_xl
from .help import help
from .set_dir import set_dir

type CommandFn = Callable[..., None]

COMMANDS: dict[str, CommandFn] = {
    "merge": merge,
    "importall": import_all,
    "importcsv": import_csv,
    "importxl": import_xl,
    "exit": exit_app,
    "files": show_files,
    "cols": show_cols,
    "drop": drop_file,
    "data": show_data,
    "rename": rename_file,
    "help": help,
    "setdir": set_dir,
}


def cmd_exists(cmd: str) -> bool:
    return cmd in COMMANDS


def execute_cmd(cmd: str, *args: Any) -> None:
    COMMANDS[cmd](*args)


def cmd_expected_args(cmd: str) -> int:
    return len(inspect.signature(COMMANDS[cmd]).parameters)-1
