
"""Модуль загрузки и сохранения задач"""


def load_collection(task_list, file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line:
                    task_list.append(line)

    except FileNotFoundError:
        pass

    return task_list


def save_collection(task_list, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for task in task_list:
            file.write(f"{task}\n")
