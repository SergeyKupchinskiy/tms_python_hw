# 2. Создать словарь, где ключ - это код страны, а значение - это количество городов.
import json
from collections import defaultdict


with open('city.list.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

country_dict = defaultdict(int)

for city in data:
    country_code = city.get('country')
    if country_code:
        country_dict[country_code] += 1

country_dict = dict(country_dict)

for country, count in country_dict.items():
    print(f'{country}: {count}')