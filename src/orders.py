import datetime
from menu import display_menu

orders = []

def make_order(menu, orders):
    print("\n=== Оформлення замовлення ===")
    if not menu:
        print("Меню порожнє, неможливо оформити замовлення.")
        return
    
    display_menu(menu)
    order_items = []
    total_price = 0
    
    while True:
        dish_id = input("Введіть ID страви для додавання до замовлення (або 'q' для завершення): ").strip()
        if dish_id.lower() == 'q':
            break
        
        try:
            dish_id = int(dish_id)
        except ValueError:
            print("Помилка: Введіть коректний числовий ID.")
            continue
        
        dish = next((d for d in menu if d["id"] == dish_id), None)
        if not dish:
            print(f"Страва з ID {dish_id} не знайдена.")
            continue
        
        quantity = int(input(f"Введіть кількість для '{dish['name']}': ").strip())
        if quantity <= 0:
            print("Кількість повинна бути більшою за 0.")
            continue
        
        order_items.append({"dish": dish, "quantity": quantity})
        total_price += dish["price"] * quantity
        print(f"Додано {quantity} шт. '{dish['name']}' до замовлення.")

    if not order_items:
        print("Замовлення порожнє.")
        return
    
    order_id = max((order["id"] for order in orders), default=0) + 1
    order = {
        "id": order_id,
        "items": order_items,
        "total_price": total_price,
        "timestamp": datetime.datetime.now(),
        "status": "в підготовці"
    }
    orders.append(order)
    
    print(f"\nЗамовлення створено! Номер замовлення: {order_id}")
    print(f"Загальна сума: {total_price} EUR")


def check_order_status(orders):
    print("\n=== Перевірка статусу замовлення ===")
    order_id = input("Введіть номер замовлення: ").strip()
    
    try:
        order_id = int(order_id)
    except ValueError:
        print("Помилка: Введіть коректний номер замовлення.")
        return
    
    order = next((o for o in orders if o["id"] == order_id), None)
    if not order:
        print(f"Замовлення з номером {order_id} не знайдено.")
        return
    
    print(f"\nЗамовлення #{order_id}")
    print(f"Час оформлення: {order['timestamp']}")
    print(f"Статус: {order['status']}")
    print("Склад замовлення:")
    for item in order["items"]:
        print(f" - {item['dish']['name']} x{item['quantity']} ({item['dish']['price']} EUR за одиницю)")
    print(f"Загальна сума: {order['total_price']} EUR")
