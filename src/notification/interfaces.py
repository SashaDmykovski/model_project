from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def send(self, recipient: str) -> str:
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass
