import requests, json
apiKey = "a45183feed60f244d420ab6dda45d92c"
burl = "http://api.openweathermap.org/data/2.5/weather?"

def getWeatherInfo(cityName):

    comp_url = burl + "appid=" + apiKey + "&q=" + cityName
    raspuns = requests.get(comp_url) #Raspusul OpenWeather API dc cod =! 404 ar trebui sa mearga
    x = raspuns.json()
    if x["cod"] != "404":
        y = x["main"]
        global current_temperature_celsius
        global current_pressure
        global current_humidiy
        global weather_description
        current_temperature_kelvin = y["temp"]
        current_temperature_celsius = int(float(current_temperature_kelvin) - 273.15)
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
