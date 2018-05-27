import requests
import os
import time
import pymongo
from pymongo import MongoClient

dbHost = os.environ['SERVICE_MONGODB_HOST']
dbPort = int(os.environ['SERVICE_MONGODB_PORT'])
url = os.environ['SERVICE_ADDRESS'] + 'temperature.json'

client = MongoClient(dbHost, dbPort)
db = client[os.environ['SERVICE_MONGODB_NAME']]

while True:
    response = requests.get(url)
    print("Received: " + response.text)
    db.temperatures.insert_one(response.json())
    time.sleep(5)