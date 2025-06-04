# Напишите функцию make_sentence, которая принимает один именованный
# аргумент words, который должен быть списком строк, и возвращает строку,
# составленную из элементов списка, разделенных пробелами и
# заканчивающуюся точкой. Если аргумент words не указан, то по умолчанию
# используется список ["This", "is", "a", "sentence"].


def make_sentence(words=None):
    if words is None:
        words = ["This", "is", "a", "sentence"]
    new_string = ' '.join(words) + '.'
    return new_string

print(make_sentence())
print(make_sentence(words=["Teach", "me", "skills"]))