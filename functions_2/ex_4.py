# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий квадраты этих чисел. Используйте функцию map и lambda.


def squaring(int):
    return list(map(lambda x: x ** 2, list_1))

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = squaring(list_1)
print(list_2)