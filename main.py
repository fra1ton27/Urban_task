calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    string_info = []
    string_info.append(len(string))  # Длина строки
    string_info.append(string.upper())  # Строка в верхнем регистре
    string_info.append(string.lower())  # Строка в нижнем регистре
    return string_info

def is_contains(string, list_to_search):
    count_calls()
    # Приводим строку к нижнему регистру для проверки
    string = string.lower()

    # Проверяем наличие строки в массиве list_to_search
    if string in list_to_search:
        return True
    else:
        return False

# Основной блок программы
str_input = input('Введите произвольную строку: ')
info = string_info(str_input)  # Сохраняем результат string_info
print("Информация о строке:", info)
print("Содержится ли строка в массиве?:", is_contains(str_input, info))
print("Количество вызовов функций:", count_calls())
