# Напишите функцию print_info, которая принимает произвольное
# количество именованных аргументов (**kwargs) и выводит их в формате
# "key: value" по одной паре на строку. Напоминаю, что kwargs в функции
# будет словарем. Если функции не передано ни одного аргумента, она должна
# вывести "No info given.".


def print_info(**kwargs):
    if not kwargs:
        print("No info given.")
    else:
        for key, value in kwargs.items():
            print(f'{key}: {value}')

print_info(name="Sergey", age="32", city="Rostov-on-Don")
print("-" * 50)
print_info()