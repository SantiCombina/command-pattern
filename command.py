from abc import ABC, abstractmethod
from light import Light
from television import Television

# Interfaz Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Comandos concretos para encender y apagar la luz
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()
    
    def undo(self):
        self.light.on()

# Comandos concretos para encender y apagar la televisión
class TVOnCommand(Command):
    def __init__(self, television: Television):
        self.television = television

    def execute(self):
        self.television.on()

    def undo(self):
        self.television.off()

class TVOffCommand(Command):
    def __init__(self, television: Television):
        self.television = television

    def execute(self):
        self.television.off()

    def undo(self):
        self.television.on()