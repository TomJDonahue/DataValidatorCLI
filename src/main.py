import pandas as pd
from dictionary import DataDictionary
from events import register_event
from shell import Shell
from settings import init_settings

if __name__ == "__main__":
    init_settings()
    model = DataDictionary()

    # model.create("file1", pd.read_csv("file1.csv"))
    # model.create("file2", pd.read_csv("file2.csv"))

    view = Shell(model)

    register_event("*", view.display_message)

    view.run()
