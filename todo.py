tasks = []

def add_task():
    text = input("Введите задачу: ")
    tasks.append(text)
    print("Задача добавлена.")

def main():
    while True:
        print("\n1. Добавить задачу")
        print("4. Выход")
        choice = input("Выберите пункт: ")
        if choice == "1":
            add_task()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный пункт.")

if __name__ == "__main__":
    main()
