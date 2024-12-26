numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # исходный список
primes = [] # список для простых чисел
not_primes = [] # список для составных чисел
is_prime = True # переменная для проверки

# Запускаем цикл для прохода по списку
for i in range(len(numbers)):
    # Зададим переменную для значения списка
    num = numbers[i]
    # В нашем решении число 1 является исключением, поэтому заранее будем делать проверку на него
    if num == 1:
        continue
    # Запускаем вложенный цикл, который будет проверять делители
    for j in range(2, num):
        is_prime = True
        if num % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим результат
print(primes)
print(not_primes)