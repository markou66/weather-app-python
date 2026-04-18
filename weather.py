from weather_service import get_weather

while True:
    city = input(str("Cidade: ")).strip()

    while city == "":
        print('Digite uma cidade...')
        city = input("Cidade: ").strip()



    weather = get_weather(city)

    if weather:
        print(f"{weather['cidade']}")
        print(f"{weather['temp']:.1f}°C - {weather['descricao']}")
        print(f"Máx: {weather['max']}°C | Mín: {weather['min']}°C")
        print(f"Sensação: {weather['sensacao']}°C")
        print(f"Umidade: {weather['umidade']}%")
    else:
        print("Erro ao buscar dados")

    again = input("\nDeseja consultar outra cidade? (s/n): ").strip().lower()

    if again != "s":
        print("Encerrando...")
        break
