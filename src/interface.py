from data import menu_items
from orders import OrderSystem
from menu import Menu
import ui

order_system = OrderSystem(menu_items)
menu_system = Menu(menu_items)


class RoleInterface:
    @staticmethod
    def show_role_menu():
        """Main role selection menu."""
        while True:
            ui.print_centered("==== Role Selection ====")
            print("1. Client")
            print("2. Restaurateur")
            print("3. Exit")

            choice = input("Select a role (1-3): ").strip()
            role_actions = {
                "1": BuyerInterface.show_menu,
                "2": RestaurateurInterface.show_menu,
                "3": RoleInterface.exit_program,
            }

            ui.loading_animation()

            action = role_actions.get(choice)
            if action:
                action()
            else:
                ui.print_error("Invalid choice. Please try again.")

    @staticmethod
    def exit_program():
        """Exit the program."""
        ui.loading_animation()
        print("\nThank you for using the system!")
        exit()


class BuyerInterface:
    @staticmethod
    def show_menu():
        """Menu for the customer."""
        while True:
            ui.print_centered("===== Client: Operations Menu =====")
            print("1. Show restaurant menu")
            print("2. Make an order")
            print("3. Check order status")
            print("4. Cancel order")
            print("5. Search dish by name")
            print("6. Return to role selection")

            choice = input("Select an option (1-6): ").strip()
            buyer_actions = {
                "1": lambda: menu_system.display(),
                "2": lambda: order_system.make_order(order_system.menu),
                "3": lambda: order_system.check_order_status(),
                "4": lambda: order_system.cancel_order(),
                "5": lambda: menu_system.search_dish_by_name(),
                "6": RoleInterface.show_role_menu,
            }

            ui.loading_animation()

            action = buyer_actions.get(choice)
            if action:
                action()
            else:
                ui.print_error("Invalid choice. Please try again.")

class RestaurateurInterface:
    @staticmethod
    def show_menu():
        """Menu for the restaurateur."""
        while True:
            ui.print_centered("===== Restaurateur: Operations Menu =====")
            print("1. Show restaurant menu")
            print("2. Add a new dish")
            print("3. Edit a dish")
            print("4. Remove a dish")
            print("5. Process an order")
            print("6. Search dish by name")
            print("7. Return to role selection")

            choice = input("Select an option (1-7): ").strip()
            restaurateur_actions = {
                "1": lambda: menu_system.display(),
                "2": lambda: menu_system.add_dish(),
                "3": lambda: menu_system.edit_dish(),
                "4": lambda: menu_system.remove_dish(),
                "5": lambda: order_system.process_order(),
                "6": lambda: menu_system.search_dish_by_name(),
                "7": RoleInterface.show_role_menu,
            }
            
            ui.loading_animation()
            
            action = restaurateur_actions.get(choice)
            if action:
                action()
            else:
                ui.print_error("Invalid choice. Please try again.")
