from src.commands.command_base import CommandArgs, Command
from src.commands.factory import generate_cmd_and_args, COMMANDS


def parse_commands(commands: str) -> tuple[Command, CommandArgs]:
    split_commands = commands.split()
    command = split_commands[0]
    arguments = [args for args in split_commands[1:] if args != '']
    print(f'Debug(parse_commands): Arguments: {arguments}')
    command, arguments = generate_cmd_and_args(command, arguments)
# TODO incorporate Help
    # if arguments and arguments[0] == '-h':
    #     return commands, ['-h']

    return command, arguments


def validate_help(args: list[str]):
    if len(args) > 0 and args[0] == '-h':
        return True
    return False


def run_shell():
    while True:
        user_input = input("tell me what you want ")
        if user_input == "T":  # TODO: Remove this if block
            quit()

        try:
            command, args = parse_commands(user_input)
        except TypeError:
            print(f"Incorrect args provided for command")
        else:
            command.execute(args)
