# Система сповіщень (Notification System)

## Опис проєкту
Проєкт демонструє використання шаблонів проектування:
- **Factory Method** (створення різних типів повідомлень: Email, SMS, Push)
- **Decorator** (додавання форматування до повідомлень: заголовок, підпис, рамка)
- **Observer** (підписка користувачів та розсилка повідомлень усім підписникам)

## Структура проєкту
```
notification_system/
│
├── src/
│   └── notification/
│       ├── interfaces.py     # Інтерфейси Message та Observer
│       ├── factory.py        # Factory Method
│       ├── decorators.py     # Decorator Pattern
│       ├── observer.py       # Observer Pattern
│       └── main.py           # Запуск прикладу
│
├── tests/
│   ├── test_factory.py       # Тести для Factory Method
│   ├── test_decorator.py     # Тести для Decorator
│   └── test_observer.py      # Тести для Observer
│
├── docs/
│   ├── uml.puml              # Файл PlantUML для діаграми
│   └── README.md             # Цей файл
│
└── requirements.txt
```

## Опис шаблонів

### Factory Method
- Абстрагує процес створення об’єктів повідомлень.
- `MessageFactory.create_message(channel)` повертає конкретний екземпляр:
  - `EmailMessage`, `SMSMessage`, `PushMessage`
- **Перевага:** Легко додати новий тип повідомлення, не змінюючи клієнтський код.

### Decorator
- Дозволяє динамічно «обгортати» об’єкт повідомлення додатковими функціональностями.
- Декоратори:
  - `HeaderDecorator` — додає заголовок до тексту.
  - `FooterDecorator` — додає підпис вкінці.
  - `BorderDecorator` — додає рамку навколо повідомлення.
- **Перевага:** Можна комбінувати декоратори у будь-якому порядку.

### Observer
- Дозволяє клієнтам (User) підписуватися на отримання повідомлень.
- `NotificationCenter` зберігає список підписників і розсилає їм повідомлення через метод `notify`.
- **Перевага:** Додавання нових підписників не вимагає зміни логіки центру розсилки.
