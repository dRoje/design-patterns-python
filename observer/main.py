from weatherStation import WeatherStation


ws = WeatherStation()


# simulate change
ws.weatherData.setMeasurements(80, 65, 30.4)
ws.weatherData.setMeasurements(82, 70, 29.2)
ws.weatherData.setMeasurements(78, 90, 29.2)
