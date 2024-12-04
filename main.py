import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from interface import RoleInterface
from ui import print_header

def main():
    print_header("=== Restaurant automation system ===")
    print("Welcome to our system!")
    print("Use the CLI to interact with the system.")

    RoleInterface.show_role_menu()

if __name__ == "__main__":
    main()