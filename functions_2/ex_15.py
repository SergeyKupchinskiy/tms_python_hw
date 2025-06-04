# Напишите декоратор retry_five, который повторяет вызов декорируемой
# функции 5 раз.


def retry_five(func):
    def wrapper(*args, **kwargs):
        for i in range(5):
            try:
                return func(*args, **kwargs)
            except:
                pass
        return func(*args, **kwargs)
    return wrapper

@retry_five
def greetings():
    print("Привет!")

greetings()