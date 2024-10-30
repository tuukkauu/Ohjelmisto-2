import json
import requests

paikkakunta = input("Kirjoita paikkakunta, josta haluat säätiedot: ")

pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid=675580857e1d1c704c0e085cc9a06ef9"

vastaus = requests.get(pyynto).json()

celcius = - 273.15

lampotila = vastaus["main"]["temp"] + celcius
lamp_tuntuu = vastaus["main"]["feels_like"] + celcius
kuvaus = vastaus["weather"][0]["description"]

print(f"Lämpötila on {lampotila:.1f} Celsiusta ja tuntuu kuin {lamp_tuntuu:.1f} Celsiusasteelta. Sään kuvaus:"
      f" {kuvaus}.")
