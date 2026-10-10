"""
Модуль дополнительных функций
"""


def check_confirm(action: str) -> bool:
    confirm = input("Точно? (Y/N): ").strip().lower()

    if confirm in ("y", "д", "да", "yes"):
        print(action)
        return True

    print("Отмена")
    return False
