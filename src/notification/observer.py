from typing import List
from .interfaces import Observer

class User(Observer):
    def __init__(self, name: str):
        self.name = name
        self.inbox: List[str] = []

    def update(self, message: str) -> None:
        self.inbox.append(f"{self.name} received: {message}")

class NotificationCenter:
    def __init__(self):
        self._subscribers: List[Observer] = []

    def subscribe(self, user: Observer) -> None:
        self._subscribers.append(user)

    def unsubscribe(self, user: Observer) -> None:
        self._subscribers.remove(user)

    def notify(self, message: str) -> None:
        for subscriber in self._subscribers:
            subscriber.update(message)
