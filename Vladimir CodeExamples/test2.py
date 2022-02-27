"""
Send data to Firestore database

python code testing

using data structure : Nested data in documents

"""

import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./csgps-saa-serviceAccountKey.json")
firebase_admin.initialize_app(cred)
#'databaseURL': 'https://csgps-saa.firebaseio.com/'
db = firestore.client()
doc_ref = db.collection(u'gps')

#document id generator test
# may only work for one test
# if the script stops and then runs again
# docID will generate a new id and will not use the id from previous iteration
#docID = doc_ref.document()

print("Sending Data to Firebase")
print("----------------------------------------")
print()

#infinite while loop
while True:
  
  #floating point values
  lat = 60.700100999
  lng = -24.498891283

  #printing out the values by converting them to str
  print('Latitude: {}'.format(str(lat)))
  print('Longitude: {}'.format(str(lng)))
  print()

  data = {
    u'latitude': lat,
    u'longitude': lng,
  }

  #location = firestore.GeoPoint(lat,lng)
  data2 = {
    u'bus-0': firestore.GeoPoint(lat, lng)
  }
  doc_ref.document(u'njxdjFQVd4HT7srHCIrN').set(data2)
  doc_ref.document(u'pSRl3zbL1okrGZFXuknW').set(data)
  #doc_ref.add(data)

  #testing using docID
  #docID.set(data)
  
  time.sleep(2)
  #pause 2 seconds