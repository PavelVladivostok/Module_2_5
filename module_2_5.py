# Функция с параметром


def get_matrix(n, m, value): #  функция принемающая
    matrix = [] # создания пустого списка
    for i in range(n): #Кол-во списков
        matrix.append([]) # Добавления размера списка
        for j in range(m): #Кол-во чисел
            matrix[i].append(value)# Добавления числа пользователя
    print(matrix) # отображения матрици


get_matrix(2, 2, 10) # Запрос функции
get_matrix(3, 5, 42) # Запрос функции
get_matrix(4, 2, 13) # Запрос функции