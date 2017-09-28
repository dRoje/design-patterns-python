from display import DisplayElement
from observer import Observer
from subject import Subject
from weatherData import WeatherData

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        self.temperature = None
        self.humidity = None
        # register/subscribe to weatherData
        assert isinstance(weatherData, Subject)
        weatherData.registerObserver(self)

    def update(self, observable, *args):
        assert isinstance(observable, WeatherData)
        wd = observable
        self.temperature = wd.getTemperature()
        self.humidity = wd.getHumidity()
        self.display()

    def display(self):
        print "Current conditions: " + str(self.temperature) + "F degrees and " + str(self.humidity) + "% humidity "
