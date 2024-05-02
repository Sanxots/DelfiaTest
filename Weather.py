import requests

def get_weather(api_key, city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            # Extrair informações meteorológicas do JSON de resposta
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            # Retornar as informações meteorológicas
            return {
                'description': weather_description,
                'temperature': temperature
            }
        else:
            print(f"Erro ao obter dados: {data['message']}")
            return None
    except Exception as e:
        print(f"Erro ao processar solicitação: {e}")
        return None

# Chave de API OpenWeatherMap
api_key = '84a34557019c076ef0bfebe91fcb5cdb'

# Cidade para obter informações meteorológicas (Itatiba)
city = 'Itatiba'

# Obter informações meteorológicas
weather_data = get_weather(api_key, city)

# Exibir informações meteorológicas
if weather_data:
    print(f"Cidade: {city}")
    print(f"Descrição do tempo: {weather_data['description']}")
    print(f"Temperatura: {weather_data['temperature']}°C")
else:
    print("Falha ao obter informações meteorológicas.")
