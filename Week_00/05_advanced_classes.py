###
### Challenge - Dog Inheritance
###

class GermanShepherd(Dog):
    pass

###
### Challenge - Dessert Inheritance
###

class Dessert:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def healthy(self):
        return self.calories < 200

    def delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name, calories, flavor):
        super().__init__(name, calories)
        self.flavor = flavor

    def delicious(self):
        return False if self.flavor == 'black licorice' else super().delicious() 


###
### Challenge - City JSON
###

def city_info(response):
    response = response[0]
    lat_lon = response['latt_long'].split(',')
    return {'City': response['title'], 'Lat': float(lat_lon[0]), 'Lon': float(lat_lon[1])}


###
### Challenge - Weather JSON
###

import datetime

def weather_forecast(response):
    today_date = datetime.date.today()
    tomorrow_date = today_date + datetime.timedelta(days = 1)
    tom_forecast = ""
    forecasts = response.get("consolidated_weather", [])
    for forecast in forecasts:
        if str(tomorrow_date) == str(forecast.get('applicable_date')):
            tom_forecast = forecast.get("weather_state_name", "unknown")
            break
    if not tom_forecast:
        tom_forecast = "unknown"
    city = response.get("title", "unknown")
    return f"The weather in {city} tommorow is {tom_forecast}"
