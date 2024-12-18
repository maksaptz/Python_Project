immutable_var = (1, "Good")
print(immutable_var)
temp_list = list(immutable_var)  # Преобразуем кортеж в список
temp_list[0] = 2 # Изменяем элемент в списке
immutable_var = tuple(temp_list)  # Возвращаем данные обратно в кортеж
print(immutable_var)
mutable_list = [1, 2]
mutable_list[0] = 4
mutable_list[1] = 3
print(mutable_list)