import json
import requests

API = 'a5f7d3eec7cfdda37fc32c88f7102558'
lat = '43.110717'
lon = '12.390828'
dst = 'C:/xampp/htdocs/ITTSWeather/'

link = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly,daily&appid={API}&units=metric'
response = requests.get(link).json()

with open(dst + 'data.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, ensure_ascii=False, indent=4)

result = f"La temperatura attuale è di {response['current']['temp']}°C"

print(result)
