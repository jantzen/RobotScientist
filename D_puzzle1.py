# D_puzzle1.py

""" Ground truth: temperature alone causes the color.
"""
from __future__ import print_function
from sense_hat import SenseHat
import time

sense = SenseHat()

try:

    print("Temperature" + 9*" " + "Humidity" + 9*" " + "Pressure" + 9*" " + " MagneticField\n\n")

    while True:
        # measure variables
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        raw = sense.get_compass_raw()
        m_field = raw['x']**2 + raw['y']**2 + raw['z']**2
        
        t = int(min([max([(temperature - 27.) * 255. / 20., 0]), 255]))
        
        color = [t, 0, 255 - t]
        
        t_out = str(temperature) + 5*" "
        h_out = str(humidity) + 5*" "
        p_out = str(pressure) + 5*" "
        m_out = str(m_field) + 5*" "


        print(t_out + h_out + p_out + m_out, end='\r')

        sense.set_pixels(64 * [color])
        
        time.sleep(0.1)

except KeyboardInterrupt:
    sense.set_pixels(64 * [0,0,0])
