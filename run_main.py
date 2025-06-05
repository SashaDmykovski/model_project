import subprocess
import sys

def main():
    print("=================================")
    print("Запуск основного скрипту (src.main)")
    print("=================================")
    result = subprocess.run([sys.executable, "-m", "src.main"], check=False)
    if result.returncode != 0:
        print("Помилка: запуск main завершився з помилкою.")
    else:
        print("Основний скрипт виконався успішно.")

if __name__ == "__main__":
    main()
