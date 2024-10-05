from src.view.view import View

class Controller:
    def __init__(self, model, view: View) -> None:
        self.model = model
        self.view = view

        view.run()