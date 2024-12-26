numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # Исходный список
primes = [] # Список для простых чисел
not_primes = [] # Список для составных чисел
is_prime = True # Переменная для проверки

# Запускаем цикл для прохода по списку
for i in range(len(numbers)):
    # Зададим переменную для значения списка
    num = numbers[i]
    # Число 1 является исключением, поэтому заранее будем делать проверку на него
    if num == 1:
        continue
    # Запускаем вложенный цикл, который будет проверять делители
    for j in range(2, num):
        is_prime = True
        if num % j == 0:
            is_prime = False
            break
    # Проверяем на простоту
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим результат
print('Primes:', primes)
print('Not Primes:', not_primes)