from src.shell.core import run_shell
import pandas as pd
from src.data.dictionary import dataframes

if __name__ == "__main__":
    dataframes['file1'] = pd.read_csv('file1.csv')
    dataframes['file2'] = pd.read_csv('file2.csv')

    run_shell()
