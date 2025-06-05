import pytest
from src.notification.factory import MessageFactory
from src.notification.decorators import HeaderDecorator, FooterDecorator, BorderDecorator

def test_header_decorator_only():
    base_msg = MessageFactory.create_message("email")
    msg = HeaderDecorator(base_msg)
    result = msg.send("Alice")
    assert result.startswith("[HEADER] ")
    assert "Email sent to Alice" in result

def test_footer_decorator_only():
    base_msg = MessageFactory.create_message("sms")
    msg = FooterDecorator(base_msg)
    result = msg.send("Bob")
    assert result.endswith(" [FOOTER]")
    assert "SMS sent to Bob" in result

def test_border_decorator_only():
    base_msg = MessageFactory.create_message("push")
    msg = BorderDecorator(base_msg)
    result = msg.send("Dave")
    assert result.startswith("*** ")
    assert result.endswith(" ***")
    assert "Push notification sent to Dave" in result

def test_combined_decorators_order():
    base_msg = MessageFactory.create_message("email")
    msg = BorderDecorator(FooterDecorator(HeaderDecorator(base_msg)))
    result = msg.send("Everyone")
    # Повинне виглядати як: "*** [HEADER] Email sent to Everyone [FOOTER] ***"
    assert result.startswith("*** [HEADER] ")
    assert "[FOOTER] ***" in result

def test_nested_decorator_multiple_levels():
    base_msg = MessageFactory.create_message("sms")
    msg1 = HeaderDecorator(base_msg)
    msg2 = BorderDecorator(msg1)
    msg3 = FooterDecorator(msg2)
    result = msg3.send("X")
    assert result.startswith("*** [HEADER] SMS sent to X")
    assert result.endswith(" [FOOTER]")

def test_decorator_does_not_change_base_class():
    base_msg = MessageFactory.create_message("sms")
    decorated = HeaderDecorator(base_msg)
    assert hasattr(decorated, "send")
    # Перевірка, що оригінальний метод send все ще викликається
    assert decorated.send("Y").startswith("[HEADER]")

def test_invalid_recipient_string_formatting():
    base_msg = MessageFactory.create_message("email")
    msg = BorderDecorator(FooterDecorator(HeaderDecorator(base_msg)))
    # Якщо передати порожній рядок, має повернути правильну рядкову структуру
    result = msg.send("")
    assert "[HEADER]" in result
    assert "[FOOTER]" in result
    assert result.startswith("***") and result.endswith("***")
