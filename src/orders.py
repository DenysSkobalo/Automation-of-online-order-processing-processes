import datetime
from collections import deque


class OrderSystem:
    def __init__(self, menu_items):
        self.menu = menu_items
        self.orders_dict = {}
        self.order_queue = deque()

    @staticmethod
    def display_menu(menu):
        """Displays the restaurant's menu."""
        if not menu:
            print("\nThe menu is empty.")
            return

        print("\n=== Restaurant Menu ===")
        for dish_id, dish in menu.items():
            print(f"ID: {dish_id} | Name: {dish['name']} | Price: {dish['price']} EUR")
            print(f"   Category: {dish['category']} | Allergens: {', '.join(dish['allergens'])}")
            print(f"   Description: {dish['description']}")
            print("-" * 40)

    def make_order(self, menu):
        """Creates a new order."""
        order_items = []
        while True:
            self.display_menu(menu)
            dish_id = input("Enter the dish ID to add to the order (or 'q' to finish): ").strip()

            if dish_id.lower() == 'q':
                break

            if dish_id.isdigit() and int(dish_id) in menu:
                dish_id = int(dish_id)
                dish = menu[dish_id]

                quantity = self.get_positive_int(f"Enter the quantity for '{dish['name']}': ")
                order_items.append({"dish": dish, "quantity": quantity})
                print(f"Dish '{dish['name']}' added to the order (Quantity: {quantity}).")
            else:
                print("Invalid dish ID. Please try again.")

        if order_items:
            order_id = len(self.orders_dict) + 1
            order_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.orders_dict[order_id] = {
                "order_items": order_items,
                "timestamp": order_timestamp,
                "status": "Processing"
            }
            self.order_queue.append(order_id)
            print(f"\nOrder #{order_id} has been successfully placed! Time: {order_timestamp}")
        else:
            print("\nOrder not created, no dishes added.")

    @staticmethod
    def get_positive_int(prompt):
        """Asks the user for a positive integer."""
        while True:
            try:
                value = int(input(prompt).strip())
                if value > 0:
                    return value
                print("Please enter a value greater than 0.")
            except ValueError:
                print("Please enter a valid integer.")

    def check_order_status(self):
        """Displays the order status by its number."""
        order_id = self.get_positive_int("Enter the order number: ")

        if order_id in self.orders_dict:
            order = self.orders_dict[order_id]
            print(f"\nOrder #{order_id}")
            print(f"Creation time: {order['timestamp']}")
            print(f"Status: {order['status']}")
            print("\nDishes in the order:")
            total_price = sum(
                item["dish"]["price"] * item["quantity"] for item in order["order_items"]
            )
            for item in order["order_items"]:
                print(f"- {item['dish']['name']} x{item['quantity']} ({item['dish']['price']} EUR each)")
            print(f"\nTotal order amount: {total_price:.2f} EUR")
        else:
            print("Order with this number not found.")

    def cancel_order(self):
        """Cancels the order if less than 5 minutes have passed since it was placed."""
        order_id = self.get_positive_int("Enter the order number to cancel: ")

        if order_id in self.orders_dict:
            order_time = datetime.datetime.strptime(self.orders_dict[order_id]["timestamp"], "%Y-%m-%d %H:%M:%S")
            elapsed_time = (datetime.datetime.now() - order_time).total_seconds()

            if elapsed_time <= 300:
                del self.orders_dict[order_id]
                print(f"Order #{order_id} has been successfully canceled.")
            else:
                print(f"Order #{order_id} cannot be canceled (more than 5 minutes have passed).")
        else:
            print("Order with this number not found.")

    def process_order(self):
        """Processes the next order in the queue."""
        if not self.order_queue:
            print("\nNo orders to process.")
            return

        order_id = self.order_queue.popleft()
        order = self.orders_dict.get(order_id)

        if order:
            order["status"] = "Being processed"
            print(f"\nProcessing order #{order_id}")
            total_price = sum(
                item["dish"]["price"] * item["quantity"] for item in order["order_items"]
            )
            for item in order["order_items"]:
                print(f"- {item['dish']['name']} x{item['quantity']} ({item['dish']['price']} EUR each)")
            print(f"\nTotal order amount: {total_price:.2f} EUR")
            order["status"] = "Completed"
            print(f"Order #{order_id} has been successfully completed!")
        else:
            print(f"Order #{order_id} not found.")
