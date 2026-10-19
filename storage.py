
"""Модуль загрузки и сохранения задач"""
from storage import load_collection, save_collection, insure_save_file
from pathlib import Path

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

def insure_save_file(file_name="saves.txt"):
    save_path = Path(file_name)

    if not save_path.exists():
        save_path.touch()
