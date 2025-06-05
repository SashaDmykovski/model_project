from .interfaces import Message

class MessageDecorator(Message):
    def __init__(self, message: Message):
        self._message = message

    def send(self, recipient: str) -> str:
        return self._message.send(recipient)

class HeaderDecorator(MessageDecorator):
    def send(self, recipient: str) -> str:
        return "[HEADER] " + super().send(recipient)

class FooterDecorator(MessageDecorator):
    def send(self, recipient: str) -> str:
        return super().send(recipient) + " [FOOTER]"

class BorderDecorator(MessageDecorator):
    def send(self, recipient: str) -> str:
        return "*** " + super().send(recipient) + " ***"
