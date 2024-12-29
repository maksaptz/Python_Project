# Задаем счетчик вызова функций
calls = 0

# Создаем функцию, которая будет подсчитывать кол-во вызовов
def count_calls():
    # Импортируем переменную счетчика
    global calls
    # Повышаем счетчик при вызове функции
    calls += 1

# Создаем функцию, которая будет возвращать кортеж
def string_info(string):
    # Вызываем функцию, чтобы повысить счетчик
    count_calls()
    # Создаем кортеж в который включаем элементы согласно условию
    my_tuple = (len(string), string.upper(), string.lower())
    # Возвращаем кортеж
    return my_tuple

# Создаем функцию, которая будет проверять наличие слова в списке
def is_contains(string, list_to_search):
    # Вызываем функцию, чтобы повысить счетчик
    count_calls()
    # Приведем переменные в единый регистр
    string = string.lower()
    # Стартуем цикл в котором будем перебирать элементы списка
    for word in list_to_search:
        # Приведем переменные в единый регистр
        word = word.lower()
        # Если находим совпадение, возвращаем значение истина
        if word == string:
            return True
    # Иначе возвращаем значение ложь
    return False

# Вызовем функции и выведем результат в консоль
print(string_info('Goodman'))
print(string_info('Badman'))
print(is_contains('Good', ['bad', 'old']))
print(is_contains('Good', ['bad', 'old', 'GoOd']))
print(calls)