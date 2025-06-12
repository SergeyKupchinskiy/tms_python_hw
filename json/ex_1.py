# 1. Определить количество городов в файле
import json


with open('city.list.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

city_name = 'name'

count = sum(1 for item in data if city_name in item)

print(f'Количество городов в файле = {count}')