# Напишите код, который принимает строку и возвращает список, содержащий
# только те буквы, которые встречаются в слове “python”. Используйте функцию
# filter и оператор in.

def filter_letters(strings):
    word = "python"
    list_1 = list(filter(lambda x: x in word, strings))
    return list_1

list_1 = "Hello, world!"
list_2 = filter_letters(list_1)
print(list_2)