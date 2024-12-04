import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from interface import RoleInterface

def main():
    print("=== Система автоматизації роботи ресторану ===")
    print("Ласкаво просимо до нашої system!")
    print("Використовуйте CLI для взаємодії з системою.")

    RoleInterface.show_role_menu()

if __name__ == "__main__":
    main()