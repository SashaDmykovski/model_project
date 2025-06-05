import pytest
from src.notification.factory import MessageFactory
from src.notification.interfaces import Message

def test_create_email_message():
    msg = MessageFactory.create_message("email")
    assert isinstance(msg, Message)
    assert msg.send("Alice") == "Email sent to Alice"

def test_create_sms_message():
    msg = MessageFactory.create_message("sms")
    assert isinstance(msg, Message)
    assert msg.send("Bob") == "SMS sent to Bob"

def test_create_push_message():
    msg = MessageFactory.create_message("push")
    assert isinstance(msg, Message)
    assert msg.send("Charlie") == "Push notification sent to Charlie"

def test_invalid_message_channel_raises():
    with pytest.raises(ValueError):
        MessageFactory.create_message("fax")
