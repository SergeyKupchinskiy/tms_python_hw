# 5. Создать другой JSON файл, в который сохранить только города одной
# выбранной страны.
import json


with open("city.list.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

filter_city = [city for city in data if city['country'] == "RU"]

with open("city_RU.json", 'w', encoding='utf-8') as f:
    json.dump(filter_city, f, ensure_ascii=False, indent=4)