# ContinuousSample.py

from sense_hat import SenseHat
import time

sense = SenseHat()

try:
    print(" {:<15}  {:<15}  {:<15}  {:<15}\n\n".format("Temperature", "Humidity", "Pressure", "MagneticField"))
    while True:
        # measure variables
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        raw = sense.get_compass_raw()
        m_field = (raw['x']**2 + raw['y']**2 + raw['z']**2)**(0.5)
        # format and print the output
        print(" {:<15.4f}  {:<15.4f}  {:<15.4f}  {:<15.4f}".format(temperature, humidity, pressure, m_field), end="\r") 
        time.sleep(0.1)

except KeyboardInterrupt:
    print('\n')
