#Найти в матрице первую строку, все элементы которой
#положительны, и сумму этих элементов.

def input_matrix():
    try:
        rows = int(input("Введите количество строк в матрице: "))
        cols = int(input("Введите количество столбцов в матрице: "))
        matrix = []

        for i in range(rows):
            row = []
            for j in range(cols):
                element = int(input(f"Введите элемент [{i+1}][{j+1}]: "))
                row.append(element)
            matrix.append(row)

        return matrix

    except ValueError:
        print("Ошибка при вводе числа. Пожалуйста, введите целое число.")
        return input_matrix()

def find_first_positive_row(matrix):
    try:
        if not matrix:
            raise ValueError("Матрица пуста")

        for row_index, row in enumerate(matrix):
            all_positive = all(element>0 for element in row)
            if all_positive:
                return row_index, sum(row)

        raise ValueError("Нет строк в матрице, где все эл-ты положительны")

    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"
    finally:
        print("Операция завершена")

matrix = input_matrix()
result = find_first_positive_row(matrix)

if isinstance(result, tuple):
    row_index, sum_of_elements = result
    print(f"Первая строка с полож эл-ами {row_index+1}, сумма: {sum_of_elements}")
else:
    print(result)