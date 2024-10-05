from typing import Protocol

class View(Protocol):
    def run(self):
        ...