# 6. Для каждой страны создать свой файл JSON с данными городов. Лучше
# создать отдельную папку в PyCharm, и указать путь к новому файлу с этой
# папкой.
import json
import os


with open('city.list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

countries = {}
for city in data:
    country_code = city.get('country')
    if country_code:
        countries.setdefault(country_code, []).append(city)

for country_code, cities in countries.items():
    folder_adress = os.path.join('filtered_countries', f'city_{country_code}.json')
    with open(folder_adress, 'w', encoding='utf-8') as f:
        json.dump(cities, f, ensure_ascii=False, indent=4)