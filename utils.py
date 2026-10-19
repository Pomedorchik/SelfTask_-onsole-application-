"""
Модуль дополнительных функций
"""
import sys
from pathlib import Path

def check_confirm(action: str) -> bool:
    confirm = input("Точно? (Y/N): ").strip().lower()

    if confirm in ("y", "д", "да", "yes"):
        print(action)
        return True

    print("Отмена")
    return False

def get_base_dir():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent