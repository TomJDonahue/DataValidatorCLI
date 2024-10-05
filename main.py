import pandas as pd  # TODO: Remove This
from src.model.dictionary import DataDictionary
from src.view.shell_view import Shell
from src.controller.controller import Controller




if __name__ == "__main__":
    # TODO: This is just for ease of testing
    data = DataDictionary()
    
    data.create('file4', pd.read_csv('file1.csv'))
    data.create('file5', pd.read_csv('file2.csv'))

    print(data.read('file5'))

    view = Shell(data)

    controller = Controller(data, view)


# So a controller controls user input and writes out to the model. The view reads from the model.
# So a shell controller would spawn a shell view. A Tkinter controller would spawn a tkinter view. etc.
