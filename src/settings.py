from os import getcwd

settings = {
    "cwd": ''
}


def init_settings() -> None:
    settings['cwd'] = getcwd()
