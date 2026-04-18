import requests

from config import API_KEY, BASE_URL

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=pt_br"
    
    response = requests.get(url)

    if response.status_code !=200:
        return None
    
    data = response.json()
    main = data['main']
    weather = data['weather'][0]

    return {
        "cidade": f"{data['name']} - {data['sys']['country']}",
        "temp": main['temp'],
        "descricao": weather['description'],
        "max": main['temp_max'],
        "min": main['temp_min'],
        "sensacao": main['feels_like'],
        "umidade": main['humidity']
    }