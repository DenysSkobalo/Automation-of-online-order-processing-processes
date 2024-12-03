import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from interface import show_role_menu

def main():
    print("=== Система автоматизації роботи ресторану ===")
    print("Ласкаво просимо до нашої програми!")
    print("Використовуйте CLI для взаємодії з системою.")

    show_role_menu()


if __name__ == "__main__":
    main()

