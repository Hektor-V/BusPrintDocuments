"""
Raspberry pi 3 Model b
NEO-6M GPS Module

GPS tracker

References:
- https://tutorial.cytron.io/2020/12/09/send-data-to-firebase-using-raspberry-pi/
- https://github.com/Knio/pynmea2
- https://github.com/thisbejim/Pyrebase
- https://github.com/pyserial/pyserial

"""

import time
import serial
import io
import string
import pynmea2
import pyrebase

config = {
  "apiKey": "PS16ea5ukzWYhUjMaqeoIG6RgqSpNgEJfodPjoUZ",
  "authDomain": "csgps-saa.firebaseapp.com",
  "databaseURL": "https://csgps-saa-default-rtdb.firebaseio.com",
  "storageBucket": "csgps-saa.appspot.com"
}

#firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()

#gps module
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5.0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

print('Sending Data to Firebase Using Raspberry Pi')
print('----------------------------------------')
print()

while True:
  line = sio.readline()

  if line[0:6] == '$GPRMC':
    msg = pynmea2.parse(line)
    lat = msg.latitude
    lng = msg.longitude

    try:
      print('Latitude: {}'.format(str(lat)))
      print('Longitude: {}'.format(str(lng)))
      print()
      data = {
        'latitude': lat,
        'longitude': lng,
      }
      db.child('NEO-6M').child('1-set').set(data)

    except serial.SerialException as e:
        print('Device error: {}'.format(e))
        break
    except pynmea2.ParseError as e:
        print('Parse error: {}'.format(e))
        continue

    time.sleep(2)