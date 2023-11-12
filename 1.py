#Написать функцию, которая определяет количество разрядов
#введенного целого числа. –

def count_digits(number):
    try:
        num = int(number)

        if num < 0:
            num = abs(num)
            
        if num == 0:
            return 1
        else:
            count = 0
            while num > 0:
                count +=1
                num//= 10
            return count

    except ValueError:
        return "Ошибка: Введенное значение не явл целым числом"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"
    finally:
        print("Операция завершена")


input_number = input("Введите целое число:")
result = count_digits(input_number)
print("Кол-во разрядов:", result)