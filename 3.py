import json

# Информация о книге в виде словаря
book_info = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}

# Преобразование в строку JSON
json_string = json.dumps(book_info)
print("Строка JSON, представляющая информацию о книге:")
print(json_string)

# Преобразование строки JSON обратно в словарь
parsed_book_info = json.loads(json_string)
print("\nСловарь, полученный из строки JSON:")
print(parsed_book_info)
