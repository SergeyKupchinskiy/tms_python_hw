# Напишите функцию greet, которая принимает два именованных аргумента:
# name и language. Аргумент name должен быть строкой, а аргумент language
# должен быть одним из трех возможных значений: "en", "ru" или "fr".
# Функция должна возвращать приветствие на выбранном языке.
# Если аргумент language не указан, то по умолчанию используется "en".


def greet(name, language ='en'):
    if language == 'en':
        return f'Hello {name}'
    elif language == 'ru':
        return f'Привет {name}'
    elif language == 'fr':
        return f'Bonjur {name}'
    elif language is None:
        return f'Hello {name}'
    else:
        return 'Language not supported'

print(greet('Ivan', language='fr'))
print(greet('Claudio', language='ru'))
print(greet('Oleksey', language='en'))
print(greet('John'))
print(greet('John', language='ge'))
