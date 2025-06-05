from .interfaces import Message

class EmailMessage(Message):
    def send(self, recipient: str) -> str:
        return f"Email sent to {recipient}"

class SMSMessage(Message):
    def send(self, recipient: str) -> str:
        return f"SMS sent to {recipient}"

class PushMessage(Message):
    def send(self, recipient: str) -> str:
        return f"Push notification sent to {recipient}"

class MessageFactory:
    @staticmethod
    def create_message(channel: str) -> Message:
        if channel == "email":
            return EmailMessage()
        elif channel == "sms":
            return SMSMessage()
        elif channel == "push":
            return PushMessage()
        else:
            raise ValueError("Unknown message channel")
