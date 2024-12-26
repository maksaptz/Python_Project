# Создаем функцию
def get_matrix(n, m, value):
    # Создаем пустой список
    matrix = []
    # Внешний цикл
    for i in range(n):
        # Добавляем пустую матрицу
        matrix.append([])
        # Внутренний цикл
        for j in range(m):
        # Наполняем созданную матрицу значениями
            matrix[i].append(value)
    # Возвращаем результат
    return matrix

# Выводим ответы на консоль
print(get_matrix(2,2,10))
print(get_matrix(3,5,42))
print(get_matrix(4,2,13))
print(get_matrix(0,0,0))