import pyowm

owm = pyowm.OWM('1ba146ea396a1e63f568053174f294e0')
observation = owm.weather_at_place('svalbard')
w = observation.get_weather()

print(w.get_wind())
print(w.get_humidity())
print(w.get_temperature(unit='celsius'))


print(w.get_sunset_time("iso"))

