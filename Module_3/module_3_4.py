'''
Задача "Однокоренные":

Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word, а далее неограниченную последовательность в параметр *other_words.

Функция должна составить новый список same_words только из тех слов списка other_words, которые содержат root_word или наоборот root_word содержит одно из этих слов. После вернуть список same_words в качестве результата своей работы.

Пункты задачи:

Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
Создайте внутри функции пустой список same_words, который пополнится нужными словами.
При помощи цикла for переберите предполагаемо подходящие слова.
Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
После цикла верните образованный функцией список same_words.
Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.
'''

# Создаем функцию
def single_root_words(root_word, *other_words):
    # Создадим список для вывода
    same_words = []
    # С помощью цикла пройдемся по списку
    for word in other_words:
        # Задаем условие, в случае успеха пополняем список same_words
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    # Возвращаем результат
    return same_words

# Проверим работу функции
print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))