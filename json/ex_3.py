# 3. Подсчитать количество городов в северном полушарии, и в южном.
import json


with open('city.list.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

north_count = 0
south_count = 0

for city in data:
    coord = city.get('coord')
    lat = coord.get('lat')

    if lat > 0:
        north_count += 1
    elif lat < 0:
        south_count += 1

print(f'В северном полушарии: {north_count} городов')
print(f'В южном полушарии: {south_count} городов')
