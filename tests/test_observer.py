import pytest
from src.notification.observer import User, NotificationCenter

def test_user_update_appends_message():
    user = User("Alice")
    user.update("Test Message")
    assert len(user.inbox) == 1
    assert user.inbox[0] == "Alice received: Test Message"

def test_subscribe_and_notify_single_user():
    user = User("Bob")
    center = NotificationCenter()
    center.subscribe(user)
    center.notify("Hello")
    assert len(user.inbox) == 1
    assert user.inbox[0] == "Bob received: Hello"

def test_subscribe_multiple_users_and_notify_all():
    u1 = User("A")
    u2 = User("B")
    u3 = User("C")
    center = NotificationCenter()
    center.subscribe(u1)
    center.subscribe(u2)
    center.subscribe(u3)
    center.notify("Broadcast")
    assert "A received: Broadcast" in u1.inbox[0]
    assert "B received: Broadcast" in u2.inbox[0]
    assert "C received: Broadcast" in u3.inbox[0]

def test_unsubscribe_prevents_receiving():
    user = User("Charlie")
    center = NotificationCenter()
    center.subscribe(user)
    center.unsubscribe(user)
    center.notify("Nope")
    assert len(user.inbox) == 0

def test_subscribe_multiple_then_unsubscribe_one():
    u1 = User("X")
    u2 = User("Y")
    center = NotificationCenter()
    center.subscribe(u1)
    center.subscribe(u2)
    center.unsubscribe(u1)
    center.notify("Message")
    assert len(u1.inbox) == 0
    assert "Y received: Message" in u2.inbox[0]

def test_no_subscribers_no_error():
    center = NotificationCenter()
    # Якщо нікого не підписано, виклик notify має просто нічого не робити
    # (не кидати винятків)
    try:
        center.notify("Silent")
    except Exception as e:
        pytest.fail(f"notify() raised an exception unexpectedly: {e}")
