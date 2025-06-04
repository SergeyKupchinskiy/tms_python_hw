# Напишите функцию create_product, которая создает товар для интернет
# магазина, основываясь на переданных параметрах. Обязательными
# параметрами являются: имя, цена и категория. Необязательным параметром
# является рейтинг. Если он не был передан параметр, то по умолчанию будет
# 0. Функция должна возвращать словарь товара.


def create_product(name, price, category, rating=0):

    product = {
        "name": name,
        "price": price,
        "category": category,
        "rating": rating
    }
    return product

product_1 = create_product("playstation 5","600$", "technic", 5)
product_2 = create_product("xbox one", "500$", "technic")
print(product_1)
print(product_2)