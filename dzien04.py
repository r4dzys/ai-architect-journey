import requests
def main():
  get_weather(input("Podaj nazwę miasta, dla którego chcesz sprawdzić pogodę "))

def get_weather(city):
  r = requests.get(f'https://wttr.in/{city}')
  print(r.text)

main()
