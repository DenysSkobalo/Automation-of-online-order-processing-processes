import menu
import orders

def show_role_menu():
        while True:
            print("\n==== Вибір ролі ====")
            print("1. User")
            print("2. Restaurateur")
            print("3. Exit")

            choice = input("Виберіть роль (1-3): ").strip()

            if choice == "1":
                buyer_interface()
            elif choice == "2":
                restaurateur_interface()  
            elif choice == "3":
                print("Дякую за користування системою!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")


def buyer_interface():
     while True:
        print("\n===== Покупець: Меню операцій =====")
        print("1. Показати меню ресторану")
        print("2. Зробити замовлення")
        print("3. Перевірити статус замовлення")
        print("4. Скасувати замовлення")
        print("5. Повернутися до вибору ролі")

        choice = input("Виберіть опцію (1-4): ").strip()

        if choice == "1":
            menu.display_menu(menu.menu_items)  
        elif choice == "2":
            orders.make_order(menu.menu_items, orders.orders)  
        elif choice == "3":
            orders.check_order_status(orders.orders)  
        elif choice == "4":
            orders.cancel_order(orders.orders)
        elif choice == "5":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
            

def restaurateur_interface():
    while True:
        print("\n===== Ресторатор: Меню операцій =====")
        print("1. Показати меню ресторану")
        print("2. Додати нову страву")
        print("3. Редагувати страву")
        print("4. Видалити страву")
        print("5. Повернутися до вибору ролі")

        choice = input("Виберіть опцію (1-5): ").strip()

        if choice == "1":
            menu.display_menu(menu.menu_items)  
        elif choice == "2":
            menu.add_dish(menu.menu_items)  
        elif choice == "3":
            menu.edit_dish(menu.menu_items)  
        elif choice == "4":
            menu.remove_dish(menu.menu_items)  
        elif choice == "5":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

            
