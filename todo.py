tasks = []

def add_task():
    text = input("Введите задачу: ").strip()
    if text:
        tasks.append(text)
        print("Задача добавлена.")
    else:
        print("Задача не может быть пустой.")

def show_tasks():
    if not tasks:
        print("Список задач пуст.")
        return
    print("\nСписок задач:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Введите номер задачи для удаления: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Задача «{removed}» удалена.")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Введите число.")

def main():
    while True:
        print("\n=== Список задач ===")
        print("1. Добавить задачу")
        print("2. Вывести список задач")
        print("3. Удалить задачу")
        print("4. Выход")
        choice = input("Выберите пункт: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()
