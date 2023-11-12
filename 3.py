#Напишите программу, демонстрирующую работу try\except\finally
while True:
    try:
        user_input = input("Введите число (или 'q' для завершения): ")

        if user_input.lower() == 'q':
            break
        number = int(user_input)

        digit_sum=0
        num_str = str(number)
        for digit in num_str:
            digit_sum += int(digit)

    except ValueError:
        print("Вы ввели некоррктное число.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    else:
        print(f"Сумма цифр введенного числа {number} равна {digit_sum}")
    finally:
        print("Программа завершила выполнение.")