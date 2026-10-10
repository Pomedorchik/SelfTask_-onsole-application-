
"""
Модуль с главными функциями
"""

from viev import show_collection, show_message
from storage import save_collection
from utils import check_confirm


def create_task(task_list, file):
    name_task = input("Введите имя задачи: ").strip()

    if not name_task:
        print("Название задачи не может быть пустым")
        return

    content_task = input("Введите описание задачи: ").strip()

    if not content_task:
        print("Описание задачи не может быть пустым")
        return

    full_task = f"{name_task} | {content_task}"
    task_list.append(full_task)

    save_collection(task_list, file)
    show_message(name_task, "добавлена")


def edited_task(task_list, file):
    if not task_list:
        print("Список задач пуст")
        return

    show_collection(task_list)

    try:
        select_edit = int(
            input("Введите номер задачи для редактирования: ")
        )
    except ValueError:
        print("Нужно ввести число")
        return

    if select_edit < 1 or select_edit > len(task_list):
        print("Задачи с таким номером нет")
        return

    old_name, old_content = task_list[select_edit - 1].split(" | ", 1)

    print(f"Текущее название: {old_name}")
    print(f"Текущее описание: {old_content}")

    edit_name = input(
        "Новое имя задачи (Enter - оставить прежнее): "
    ).strip()

    edit_content = input(
        "Новое описание (Enter - оставить прежнее): "
    ).strip()

    if edit_name:
        old_name = edit_name

    if edit_content:
        old_content = edit_content

    task_list[select_edit - 1] = f"{old_name} | {old_content}"

    save_collection(task_list, file)
    show_message(old_name, "изменена")


def deleted_task(task_list, file):
    if not task_list:
        print("Список задач пуст")
        return

    show_collection(task_list)

    try:
        delete_edit = int(
            input("Введите номер задачи для удаления: ")
        )
    except ValueError:
        print("Нужно ввести число")
        return

    if delete_edit < 1 or delete_edit > len(task_list):
        print("Задачи с таким номером нет")
        return

    task_name = task_list[delete_edit - 1].split(" | ", 1)[0]

    if check_confirm(f"Задача «{task_name}» удалена"):
        task_list.pop(delete_edit - 1)
        save_collection(task_list, file)
        show_collection(task_list)
