import json

if __name__ == '__main__':
    is_running = True
    collection = []
    filename = "tasks.json"
    #try и except конструкции для обработки ошибок
    try:
       with open(filename, "r", encoding="utf-8") as file:
           collection = json.load(file)
    except FileNotFoundError:
        collection = []

    print(" Welcome")
    def show_collection(collection):
        print("=" * 30)
        if not collection:
            print("Задач нет!")
        else:
            for i, j in enumerate(collection):
                print(f"{i + 1}. {j}")

    def save_collection(collection):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(collection, file, ensure_ascii=False, indent=4)

    while is_running:
        print(f"| 1 - Просмотр задачи \n| 2 - Добавить задачу \n| 3 - Редактирование задачи \n| 4 - Удаление задачи \n| 5 - Выход ")
        choice_user = input("Введите свой выбор:")
        match choice_user:
            case '1':
                show_collection(collection)
                print("=" * 30)
                waite = input("Нажмите  Enter  для продолжения: ")
            case '2':
                name_task = input("Введите имя задачи:")
                collection.append(name_task)
                save_collection(collection)
                print(f"Задача {name_task} успешно сохронина:)")
                input("Нажмите  Enter  для продолжения: ")
            case '3' :
                print("=" * 30)
                show_collection(collection)
                print("=" * 30)
                select_edit = int(input("Введите номер задачи"))
                edit_name = input ("Укажите новое имя задачи")
                confirm = input("Вы точно уверены, что хотите изменить задачу? (y/n): ")
                if confirm == 'y':
                    print("Задача изменина:)")
                    collection[select_edit - 1] = edit_name
                    save_collection(collection)
                elif confirm == 'n':
                    print("Продолжаем работу.")
                else:
                    print("Некорректный ввод. Ожидалось 'y' или 'n'.")

            case '4':
                show_collection(collection)
                delete_task = int(input("Введите номер задачи"))
                collection.pop(delete_task - 1)
                save_collection(collection)
            case '5':
                confirm = input("Вы точно уверены, что хотите выйти? (y/n): ")
                if confirm == 'y':
                    print("Выход из программы...")
                    is_running = False
                elif confirm == 'n':
                    print("Продолжаем работу.")
                else:
                    print("Некорректный ввод. Ожидалось 'y' или 'n'.")
            case _:
                print("Такого пункта нет!")

