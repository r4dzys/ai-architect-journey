import requests
import json

def main():
  get_temp(input("Podaj nazwę miasta, dla którego chcesz sprawdzić obecnie temperaturę powietrza "))

def get_temp(city):
  r = requests.get(f'https://wttr.in/{city}?format=j1')
  data = r.json()
  temp = data['current_condition'][0]['temp_C']
  print(f"Temperatura w {city}: {temp}°C")

main()
