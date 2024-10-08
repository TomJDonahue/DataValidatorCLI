import pandas as pd  # TODO: Remove This
from src.model.dictionary import DataDictionary
from src.view.shell_view import Shell
from src.controller.shell_controller import ShellController




if __name__ == "__main__":
    # TODO: This is just for ease of testing
    model = DataDictionary()
    
    model.create('file4', pd.read_csv('file1.csv'))
    model.create('file5', pd.read_csv('file2.csv'))

    print(model.read('file5'))

    view = Shell(model)

    controller = ShellController(model, view)
