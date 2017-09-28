from weatherData import WeatherData
from currentConditionsDisplay import CurrentConditionsDisplay
from heatIndexDisplay import HeatIndexDisplay


class WeatherStation:
    def __init__(self):
        self.weatherData = WeatherData()
        self.currentConditionsDisplay = CurrentConditionsDisplay(self.weatherData)
        self.heatIndexDisplay = HeatIndexDisplay(self.weatherData)

