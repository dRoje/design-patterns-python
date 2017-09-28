from subject import Subject


class WeatherData(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def measurementsChanged(self):
        self.setChanged()
        self.notifyObservers()

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure

    def setMeasurements(self, temperature, humidity, pressure):
        # for testing
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

