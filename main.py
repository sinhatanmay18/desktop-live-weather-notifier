import json
import requests
from win10toast import ToastNotifier

n = ToastNotifier()

def getdata(url):
    r = requests.get(url)
    return r.text


jsonData = getdata("http://api.weatherapi.com/v1/current.json?key=e2e35c99db2d45ad9be150025230112&q=Bangalore&aqi=no")

data = json.loads(jsonData)

current_temperature = data['current']['temp_c']
weather_condition = data['current']['condition']['text']

result = "current_temp " + str(current_temperature) + "°C in Bengaluru" + "\n" + "Current weather condition: " + weather_condition

n.show_toast("Weather update", result, duration = 10)