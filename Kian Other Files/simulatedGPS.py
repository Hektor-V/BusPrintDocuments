
"""
Send data to Firestore database

python code testing

modified - 11/28/21 - 2:14 PM
modified - 11/28/21 - 10:08 PM
"""

import time
import google.cloud
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./csgps-saa-serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'gps')

print("Send Data to Firebase Using Raspberry Pi")
print("----------------------------------------")
print()

while True:
    lat = [37.71979, 37.71944, 37.71856, 37.71824, 37.71749, 37.71708, 37.71679, 37.71674, 37.71671, 37.71674, 37.71656, 37.71634, 37.71637, 37.71636, 37.71636, 37.71697, 37.71745, 37.71744, 37.71768, 37.7182, 37.71865, 37.71912, 37.71967, 37.72001, 37.72059, 37.7209, 37.72123, 37.72128, 37.72132, 37.72132, 37.72131, 37.72124, 37.72112, 37.72083, 37.72068, 37.72049, 37.72031, 37.71994, 37.71993]
    lng = [-97.29756, -97.29798, -97.2981, -97.29811, -97.29811, -97.298, -97.29752, -97.29672, -97.29596, -97.29509, -97.29474, -97.29404, -97.29342, -97.2928, -97.292, -97.29153, -97.29097, -97.28998, -97.28928, -97.2893, -97.28964, -97.28986, -97.28974, -97.28986, -97.28985, -97.28987, -97.28989, -97.29069, -97.29148, -97.29217, -97.29272, -97.29344, -97.29407, -97.29454, -97.29504, -97.29541, -97.29576, -97.29612, -97.2965, -97.29706]
    for x, y in zip(lat,lng):
        data = {
            u'bus-0': firestore.GeoPoint(x, y)
        }
        doc_ref.document(u'njxdjFQVd4HT7srHCIrN').set(data)
        print('Latitude: {}'.format(str(x)))
        print('Longitude: {}'.format(str(y)))
        print()
        time.sleep(2)



