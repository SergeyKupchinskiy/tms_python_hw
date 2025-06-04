# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества уникальных букв в словах.
# Используйте функцию sorted и ключ сортировки.

def unique_letter_filter(words):
    return sorted(words, key = lambda word: len(set(word)))

list_1 = ['Валенитина','Олег','Максим','Игорь','Василий','Степан']
list_2 = unique_letter_filter(list_1)
print(list_2)