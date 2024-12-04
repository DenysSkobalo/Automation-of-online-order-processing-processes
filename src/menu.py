from collections import defaultdict
import ui
class Node:
    def __init__(self, key, dish):
        """Initialization of a tree node with a key and a dish."""
        self.left = None
        self.right = None
        self.key = key
        self.dish = dish


class BST:
    def __init__(self):
        """Initialization of a binary search tree."""
        self.root = None

    def insert(self, key, dish):
        """Inserting a new dish into the tree using the key."""
        if self.root is None:
            self.root = Node(key, dish)
        else:
            self._insert(self.root, key, dish)

    def _insert(self, root, key, dish):
        """Helper function for inserting an element into the tree."""
        if key < root.key:
            if root.left is None:
                root.left = Node(key, dish)
            else:
                self._insert(root.left, key, dish)
        else:
            if root.right is None:
                root.right = Node(key, dish)
            else:
                self._insert(root.right, key, dish)

    def search(self, key):
        """Search for a dish in the tree by key."""
        return self._search(self.root, key)

    def _search(self, root, key):
        """Helper function for searching for an element in the tree."""
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def search_by_name(self, name):
        """Search for a dish by name."""
        return self._search_by_name(self.root, name.lower())

    def _search_by_name(self, root, name):
        """Helper function for searching for a dish by name in the tree."""
        if root is None:
            return None
        if root.dish['name'].lower() == name:
            return root.dish
        elif name < root.dish['name'].lower():
            return self._search_by_name(root.left, name)
        else:
            return self._search_by_name(root.right, name)


class Menu:
    def __init__(self, menu_items=None):
        """Initialization of the menu and search tree."""
        self.menu_items = menu_items if menu_items else defaultdict(dict)
        self.bst = BST()

    def load_data(self, data):
        """Load the menu from an external source."""
        self.menu_items.update(data)
        for dish_id, dish in data.items():
            self.bst.insert(dish_id, dish)
        ui.print_success("\nData successfully loaded!")

    def display(self):
        """Display the entire menu."""
        if not self.menu_items:
            ui.print_error("\nThe menu is empty.")
            return

        total_steps = 100
        print("\nLoading...")
        ui.progress_bar(range(total_steps), total_steps, prefix="Finish:")

        print()
        ui.print_line(90)
        ui.print_text_centered("=== Restaurant Menu ===")
        print(f"\n{'ID':<5} {'Name':<30} {'Price (EUR)':<15} {'Category':<20} {'Allergens':<30}")
        ui.print_line(90)
        
        for dish_id, dish in self.menu_items.items():
            print(f"{dish_id:<5} {dish['name']:<30} {dish['price']:<15} {dish['category']:<20} {', '.join(dish['allergens']):<30}")
            ui.print_line(90)

    def add_dish(self):
        """Adding a new dish to the menu."""
        name = ui.get_dish_name()
        price = float(input("Enter the price of the dish (EUR): ").strip())
        category = input("Enter the category of the dish: ").strip()
        allergens = input("List allergens separated by commas (if any): ").strip().split(",")
        description = input("Add a description for the dish: ").strip()

        new_id = max(self.menu_items.keys(), default=0) + 1

        new_dish = {
            "name": name,
            "price": price,
            "category": category,
            "allergens": [a.strip() for a in allergens if a.strip()],
            "description": description,
        }

        self.menu_items[new_id] = new_dish
        self.bst.insert(new_id, new_dish)
        total_steps = 100
        print("Storage of th dish(es)...")
        ui.progress_bar(range(total_steps), total_steps, prefix="Finish:")

        ui.print_success(f"\nDish(es) '{name}' successfully added to the menu!")

    def edit_dish(self):
        """Edit an existing dish."""
        dish_id = int(input("\nEnter the ID of the dish you want to edit: ").strip())

        total_steps = 100
        print("Loading...")
        ui.progress_bar(range(total_steps), total_steps, prefix="Finish:")


        if dish_id in self.menu_items:
            dish = self.menu_items[dish_id]
            print(f"Editing dish '{dish['name']}' (ID: {dish_id})")
            name = input(f"New name (leave empty to keep unchanged): ").strip()
            price = input(f"New price (leave empty to keep unchanged): ").strip()
            category = input(f"New category (leave empty to keep unchanged): ").strip()
            allergens = input(f"New allergens (leave empty to keep unchanged): ").strip()
            description = input(f"New description (leave empty to keep unchanged): ").strip()

            if name:
                dish["name"] = name
            if price:
                dish["price"] = float(price)
            if category:
                dish["category"] = category
            if allergens:
                dish["allergens"] = [a.strip() for a in allergens.split(",") if a.strip()]
            if description:
                dish["description"] = description

            total_steps = 100
            print("Updating...")
            ui.progress_bar(range(total_steps), total_steps, prefix="Finish:")
            ui.print_success(f"\nDish with ID {dish_id} successfully updated!")
        else:
            ui.print_error(f"\nDish with ID {dish_id} not found.")

    def remove_dish(self):
        """Remove a dish from the menu."""
        dish_id = int(input("\nEnter the ID of the dish you want to remove: ").strip())

        total_steps = 100
        print("Searching...")
        ui.progress_bar(range(total_steps), total_steps, prefix="Finish:")

        if dish_id in self.menu_items:
            dish = self.menu_items.pop(dish_id)
            ui.print_success(f"\nDish '{dish['name']}' (ID: {dish_id}) successfully removed!")
        else:
            ui.print_error(f"\nDish with ID {dish_id} not found.")

    def search_dish_by_name(self):
        """Search for a dish by name."""
        search_term = ui.get_dish_name().lower()

        total_steps = 100
        print("Searching...")
        ui.progress_bar(range(total_steps), total_steps, prefix="Finish:")

        found_dishes = [
            (dish_id, dish) for dish_id, dish in self.menu_items.items()
            if search_term in dish['name'].lower()
        ]

        if found_dishes:
            print("\nFound dishes:")
            for dish_id, dish in found_dishes:
                print(f"ID: {dish_id} | Name: {dish['name']} | Price: {dish['price']} EUR")
                print(f"Category: {dish['category']} | Allergens: {', '.join(dish['allergens'])}")
                print(f"Description: {dish['description']}")
                print("-" * 40)
        else:
            ui.print_error(f"Dish with the name '{search_term}' not found.")
