# Напишите функцию create_post, которая создает пост для блога,
# основываясь на переданных параметрах. Обязательными параметрами
# являются: заголовок, содержимое и автор. Необязательным параметром
# является категория. Если она не была передана, то по умолчанию будет
# текущая значение “general”. Функция должна возвращать словарь поста.


def create_post(title, content, author, category="general"):

    post = {
        "title": title,
        "content": content,
        "author": author,
        "category": category
    }
    return post

post_1 = create_post("My first post", "Hello, world!", "John")
post_2 = create_post("My last post", "Goodbye, world!", "Peter", category="strange things")
print(post_1)
print(post_2)