import subprocess
import sys

def main():
    print("=================================")
    print("Запуск тестів (pytest)")
    print("=================================")
    result = subprocess.run([sys.executable, "-m", "pytest"], check=False)
    if result.returncode != 0:
        print("Помилка: тести не пройшли.")
    else:
        print("Усі тести пройшли успішно.")

if __name__ == "__main__":
    main()
