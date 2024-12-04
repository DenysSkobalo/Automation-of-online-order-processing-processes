menu_items = [
    {
        "id": 1,
        "name": "Борщ",
        "price": 22.00,
        "allergens": ["буряк"],
        "description": "Традиційна українська страва",
        "category": "Супи"
    },
    {
        "id": 2,
        "name": "Вареники з картоплею",
        "price": 15.00,
        "allergens": ["глютен"],
        "description": "Вареники з м'яким картопляним пюре",
        "category": "Основні страви"
    },
    {
        "id": 3,
        "name": "Наполеон",
        "price": 7.00,
        "allergens": ["глютен", "молоко"],
        "description": "Класичний багатошаровий десерт",
        "category": "Десерти"
    }
]


def display_menu(menu):
    if not menu:
        print("\nMenu is empty.")
        return

    print("\n=== Menu resto ===")
    for dish in menu:
        print(f"ID: {dish['id']} | Назва: {dish['name']} | Ціна: {dish['price']} EUR")
        print(f"   Категорія: {dish['category']} | Алергени: {', '.join(dish['allergens'])}")
        print(f"   Опис: {dish['description']}")
        print("-" * 40)


def add_dish(menu):
    name = input("Введіть назву страви: ").strip()
    price = float(input("Введіть ціну страви (EUR): ").strip())
    category = input("Введіть категорію страви: ").strip()
    allergens = input("Перерахуйте алергени через кому (якщо є): ").strip().split(",")
    description = input("Додайте опис страви: ").strip()
    
    new_id = max((dish["id"] for dish in menu), default=0) + 1

    new_dish = {
        "id": new_id,
        "name": name,
        "price": price,
        "category": category,
        "allergens": [allergen.strip() for allergen in allergens if allergen.strip()],
        "description": description,
    }

    menu.append(new_dish)
    print(f"\nСтраву '{name}' успішно додано до меню!")


def edit_dish(menu):
    dish_id = int(input("Введіть ID страви, яку потрібно редагувати: ").strip())
    
    for dish in menu:
        if dish["id"] == dish_id:
            print(f"Редагування страви '{dish['name']}' (ID: {dish_id})")
            name = input(f"Нова назва (залиште порожнім, щоб не змінювати): ").strip()
            price = input(f"Нова ціна (залиште порожнім, щоб не змінювати): ").strip()
            category = input(f"Нова категорія (залиште порожнім, щоб не змінювати): ").strip()
            allergens = input(f"Нові алергени (залиште порожнім, щоб не змінювати): ").strip()
            description = input(f"Новий опис (залиште порожнім, щоб не змінювати): ").strip()

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

            print(f"\nСтраву з ID {dish_id} успішно оновлено!")
            return
    
    print(f"\nСтраву з ID {dish_id} не знайдено.")


def remove_dish(menu):
    dish_id = int(input("Введіть ID страви, яку потрібно видалити: ").strip())
    
    for dish in menu:
        if dish["id"] == dish_id:
            menu.remove(dish)
            print(f"\nСтраву '{dish['name']}' (ID: {dish_id}) успішно видалено!")
            return
    
    print(f"\nСтраву з ID {dish_id} не знайдено.")
