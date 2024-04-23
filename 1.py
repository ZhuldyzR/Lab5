# Создание словаря с меню кафе
menu = {
    "Американо": 3000,
    "Капучино": 3500,
    "Латте": 4500,
    "Моккачино": 3600,
    "Флэт Уайт": 3800
}

# Функция для поиска цены напитка
def find_price(drink_name):
    if drink_name in menu:
        return f"{menu[drink_name]} KRW"
    else:
        return "Напиток отсутствует в меню"

# Пример использования функции
drink = input("Введите название напитка: ")
price = find_price(drink)
print(f"Цена {drink}: {price}")
