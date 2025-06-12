# 4. Перевести в CSV файл данные по городам (координаты представить в виде
# строки значений через запятую)
import json
import csv


with open('city.list.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

with open('city.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(['id', 'name', 'country', 'coord'])

    for city in data:
        city_id = city.get('id')
        name = city.get('name')
        country = city.get('country')
        coord = city.get('coord',)
        lat = coord.get('lat')
        lon = coord.get('lon')

        coord_string = f"{lat},{lon}"

        writer.writerow([city_id, name, country, coord_string])