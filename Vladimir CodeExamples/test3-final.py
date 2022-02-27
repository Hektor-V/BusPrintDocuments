"""
Raspberry pi 3 Model b
NEO-6M GPS Module

GPS tracker - V1

References:
- https://tutorial.cytron.io/2020/12/09/send-data-to-firebase-using-raspberry-pi/
- https://github.com/Knio/pynmea2
- https://github.com/pyserial/pyserial
- https://github.com/firebase/firebase-admin-python
- https://firebase.google.com/docs/firestore

Vladimir Nava - 24/11/2021

"""

import time
import serial
import io
import string
import pynmea2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("csgps-saa-serviceAccountKey.json")
firebase_admin.initialize_app(cred)

#firebase
db = firestore.client()
doc_ref = db.collection(u'gps')

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
          u'bus-0': firestore.GeoPoint(lat, lng)
        }

      doc_ref.document(u'njxdjFQVd4HT7srHCIrN').set(data)
        
    except serial.SerialException as e:
        print('Device error: {}'.format(e))
        break
    except pynmea2.ParseError as e:
        print('Parse error: {}'.format(e))
        continue

    time.sleep(2)