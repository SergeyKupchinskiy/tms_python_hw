# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий эти же числа, умноженные на 10. Используйте функцию.

def multiplication(int):
    return list(map(lambda x: x * 10, list_1))

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = multiplication(list_1)
print(list_2)