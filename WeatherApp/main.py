#c3d2bc88b3054bc3b88141529240707

import requests
import json
import os

city = input("Enter the City : ")

url = f"http://api.weatherapi.com/v1/current.json?" \
      f"key=c3d2bc88b3054bc3b88141529240707&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(w)
print("The current weather in",city,"is", w,"dgrees")

os.system(f'powershell -Command "Add-Type -AssemblyName System.Speech; '
          f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'The current weather in {city} is {w} degrees\');"')