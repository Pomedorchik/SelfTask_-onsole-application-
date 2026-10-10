
"""
Модуль отображения информации в консоли
"""


def show_collection(task_list):
    print("=" * 40)
    print("СПИСОК ЗАДАЧ")

    if not task_list:
        print("Список задач пуст")
        print("=" * 40)
        return

    for number, task in enumerate(task_list, start=1):
        parts = task.split(" | ", 1)
        name = parts[0]
        print(f"{number}. {name}")

    print("=" * 40)

    selected_task = input(
        "Введите номер задачи для просмотра или Enter для пропуска: "
    ).strip()

    if not selected_task:
        return

    if not selected_task.isdigit():
        print("Нужно ввести номер задачи")
        return

    number = int(selected_task)

    if number < 1 or number > len(task_list):
        print("Задачи с таким номером нет")
        return

    parts = task_list[number - 1].split(" | ", 1)

    name = parts[0]
    content = parts[1] if len(parts) > 1 else "Описание отсутствует"

    print("-" * 40)
    print(f"Название: {name}")
    print(f"Описание: {content}")
    print("-" * 40)


def show_message(message=None, mess_action=None):
    if message is not None:
        print(f"Задача «{message}» успешно {mess_action}")

    input("Нажмите Enter для продолжения...")
