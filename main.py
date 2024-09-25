from src.shell.core import run_shell
import pandas as pd  # TODO: Remove This
from src.data.dictionary import dataframes  # TODO: Remove This


if __name__ == "__main__":
    # TODO: This is just for ease of testing
    dataframes['file4'] = pd.read_csv('file1.csv')
    dataframes['file5'] = pd.read_csv('file2.csv')

    run_shell()


