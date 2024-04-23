def drinks_below_price(menu, max_price):
    print(f"Напитки по цене ниже или равной {max_price} KRW:")
    for drink, price in menu.items():
        if price <= max_price:
            print(f"- {drink}: {price} KRW")

# Пример использования функции
menu = {
    "Американо": 3000,
    "Капучино": 3500,
    "Латте": 4500,
    "Моккачино": 3600,
    "Флэт Уайт": 3800
}

max_price = 3600
drinks_below_price(menu, max_price)
