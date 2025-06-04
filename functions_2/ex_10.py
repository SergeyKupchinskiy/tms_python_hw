# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества гласных букв в словах.
# Используйте функцию sorted и ключ сортировки.


def vowels_count(word):
    vowels = 'ауеяиоюэАУЕЯИОЮЭ'
    return sum(1 for letter in word if letter in vowels)

def filter_by_count(words):
    return sorted(words, key = vowels_count)

list_1 = ['Валенитина','Олег','Максим','Игорь','Василий','Степан']
list_2 = filter_by_count(list_1)
print(list_2)