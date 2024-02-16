import json
import requests
from win10toast import ToastNotifier

n = ToastNotifier()

def getdata(url):
    r = requests.get(url)
    return r.text


jsonData = getdata("YOUR-API-KEY")

data = json.loads(jsonData)

current_temperature = data['current']['temp_c']
weather_condition = data['current']['condition']['text']

result = "current_temp " + str(current_temperature) + "°C in Bengaluru" + "\n" + "Current weather condition: " + weather_condition

n.show_toast("Weather update", result, duration = 10)
