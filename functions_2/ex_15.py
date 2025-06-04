# Напишите декоратор retry_five, который повторяет вызов декорируемой
# функции 5 раз.


def retry_five(func):
    def wrapper(*args, **kwargs):
        for i in range(5):
            result = func(*args, **kwargs)
        return result
    return wrapper

@retry_five
def greetings():
    print("Привет!")

greetings()