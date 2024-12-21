from dataclasses import dataclass

from commands.factory import cmd_exists, execute_cmd, cmd_expected_args
from commands.model import Model


@dataclass
class Command:
    cmd: str
    args: list[str | int | list[str]]

    @staticmethod
    def from_string(command: str) -> "Command":
        parts = command.split()
        cmd, raw_args = parts[0], parts[1:]

        if not cmd_exists(cmd):
            raise ValueError(f"Command {cmd} does not exist.")

        parsed_args: list[str | int | list[str]] = ['' for arg in raw_args]
        # Process each argument, converting to appropriate type
        for i, arg in enumerate(raw_args):
            try:
                if arg.isnumeric():
                    parsed_args[i] = int(arg)
                else:
                    parsed_args[i] = arg
            except ValueError:
                pass
        # If extra optional arguments are added (as in the case of the merge command),
        # the parser converts the final arguments into a list.
        expected_args: int = cmd_expected_args(cmd)
        if expected_args < len(parsed_args):
            grouped_args = [str(arg) for arg in parsed_args[expected_args-1:]]
            parsed_args = [arg for arg in parsed_args[:expected_args-1]]
            parsed_args.append(grouped_args)

        return Command(cmd, parsed_args)

    def execute(self, model: Model) -> None:
        execute_cmd(self.cmd, model, *self.args)
