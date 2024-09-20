from abc import ABC,abstractmethod

class CommandArgs(ABC):
    ...

class Command(ABC):
    
    @abstractmethod
    def execute(self, args: CommandArgs):
        ...