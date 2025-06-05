from src.notification.factory import MessageFactory
from src.notification.decorators import HeaderDecorator, FooterDecorator, BorderDecorator
from src.notification.observer import User, NotificationCenter


def main():
    # Створюємо двох користувачів
    alice = User("Alice")
    bob = User("Bob")

    # Створюємо центр сповіщень і підписуємо користувачів
    center = NotificationCenter()
    center.subscribe(alice)
    center.subscribe(bob)

    # За допомогою Factory Method створюємо базове повідомлення (Email)
    msg = MessageFactory.create_message("email")

    # Огортаємо його декораторами: додаємо заголовок, підпис і рамку
    msg = HeaderDecorator(msg)
    msg = FooterDecorator(msg)
    msg = BorderDecorator(msg)

    # Відправляємо остаточне повідомлення (наприклад, «all users»)
    final_msg = msg.send("all users")
    center.notify(final_msg)

    # Друкуємо вміст «скриньок» кожного користувача
    for user in (alice, bob):
        for note in user.inbox:
            print(note)

if __name__ == "__main__":
    main()
