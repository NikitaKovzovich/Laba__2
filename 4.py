#Напишите функцию, которая будет принимать один аргумент.
# Если в функцию передаётся список, Вывести все уникальные элементы списка (которые не повторяются). Поменять местами максимальный и минимальный
#Если словарь, вывести все ключи отдельным списком. Найти ключ с минимальным значением.
#Число – определить простое,или нет.
#Строка – Найти сумму чисел строки.
#Сделать проверку со всеми этими случаями.

def process_data(data):
    if isinstance(data,list):
        unique_elements = list(set(data))
        min_index = data.index(min(data))
        max_index = data.index(max(data))
        data[min_index], data[max_index] = data[max_index], data[min_index]
        return unique_elements,data

    elif isinstance(data,dict):
        keys = list (data.keys())
        min_key = min(data, key=data.get())
        return keys,min_key

    elif isinstance(data,int):
        return is_prime(data)

    elif isinstance(data, str):
        return sum_of_numbers_in_string(data)

    else:
        return "Тип данных не поддерживается"

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


def sum_of_numbers_in_string(s):
    numbers = [int(x) for x in s if x.isdigit()]
    return sum(numbers)


def get_user_data():
    while True:
        print("Меню:")
        print("1. Ввести данные с клавиатуры")
        print("2. Список")
        print("3. Словарь")
        print("4. Число")
        print("5. Строка")
        print("0. Выход")

        choice = input("Выберите вариант (1/2/3/4/5/0): ").strip()

        if choice == "1":
            user_input = input("Введите данные с клавиатуры: ")
        elif choice == "2":
            user_input = "[2, 4, 1, 3, 5]"
        elif choice == "3":
            user_input = "{'имя': 'Иван', 'возраст': 30, 'город': 'Москва'}"
        elif choice == "4":
            user_input = "17"
        elif choice == "5":
            user_input = "abc123def456"
        elif choice == "0":
            break
        else:
            print("Неправильный выбор варианта.")
            continue

        try:
            data = eval(user_input)
            result = process_data(data)
            print(result)
        except (ValueError, SyntaxError):
            print("Некорректный ввод данных")

get_user_data()
