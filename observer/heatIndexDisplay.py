from observer import Observer
from subject import Subject
from display import DisplayElement
from weatherData import WeatherData


class HeatIndexDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        # register/subscribe to weatherData
        assert isinstance(weatherData, Subject)
        weatherData.registerObserver(self)
        self.heatIndex = None

    def update(self, observable, *args):
        assert isinstance(observable, WeatherData)
        wd = observable
        temperature = wd.getTemperature()
        humidity = wd.getHumidity()
        self.heatIndex = temperature * humidity * 0.1
        self.display()

    def display(self):
        print "heat index: " + str(self.heatIndex)
