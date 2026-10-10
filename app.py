
"""Главный модуль приложения"""

from viev import show_collection
from core import create_task, edited_task, deleted_task
from storage import load_collection
from utils import check_confirm


def main():
    name_file = "saves.txt"
    collection = load_collection([], name_file)

    is_running = True

    while is_running:
        print(
            "\n1 - Посмотреть задачи"
            "\n2 - Добавить задачу"
            "\n3 - Редактировать задачу"
            "\n4 - Удалить задачу"
            "\n5 - Выход"
        )

        choice_user = input("Введите команду: ").strip()

        match choice_user:
            case "1":
                show_collection(collection)

            case "2":
                create_task(collection, name_file)

            case "3":
                edited_task(collection, name_file)

            case "4":
                deleted_task(collection, name_file)

            case "5":
                if check_confirm("Выход из приложения"):
                    is_running = False

            case _:
                print("Неверная команда")

    print("Спасибо за использование Task Manager!")
