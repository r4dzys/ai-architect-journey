import requests
import json

def main():
  name = input("What is your name? ")
  hello(name)
  questions()
  get_temp(input("Input the name of the city, that you want to know the air temperature in "))

def hello(to="you"):
  print(f"Hello {to}, welcome to my short program!")

def questions():

  FAQ = {
    "1. What is the primary purpose of a weather forecast?":"Predicting future weather conditions for a specific location and time, allowing people to plan activities, ensure safety, and make informed decisions.",
    "2. How do meteorologists collect data for weather forecasts?":"Using a variety of tools, including weather satellites, radar, weather balloons, ground-based observation stations, and ocean buoys.",
    "3. What are some common weather forecasting models?":"Common weather forecasting models include the Global Forecast System (GFS) from the USA, the European Centre for Medium-Range Weather Forecasts (ECMWF) model, and regional models like the North American Mesoscale (NAM) model.",
    "4. What is the difference between weather and climate?":"Weather refers to the atmospheric conditions over a short period (hours to days) in a specific location (e.g., today's temperature and rain). Climate, on the other hand, describes the average weather patterns for a region over long periods (decades to centuries).",
    "5. How reliable are modern weather forecasts?":"Modern weather forecasts are highly reliable, especially for short-term predictions. A 3-day forecast is generally accurate about 90% of the time, and a 7-day forecast around 80%. Accuracy decreases as the forecast period extends, but continuous advancements in technology and modeling are improving longer-range predictions."
}
  print("Below are some frequently asked questions about the weather forecasts.")
  for q in FAQ:
    print(q, FAQ[q], sep=' - ')

def get_temp(city):
  r = requests.get(f'https://wttr.in/{city}?format=j1')
  data = r.json()
  temp = data['current_condition'][0]['temp_C']
  print(f"Current temperature in {city}: {temp}°C")

main()
