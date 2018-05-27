import requests
import os
import time
import json
import pytz
import pymongo
import datetime
from pymongo import MongoClient

dbHost = os.environ['SERVICE_MONGODB_HOST']
dbPort = int(os.environ['SERVICE_MONGODB_PORT'])
url = os.environ['SERVICE_ADDRESS'] + 'temperature.json'

client = MongoClient(dbHost, dbPort)
db = client[os.environ['SERVICE_MONGODB_NAME']]

while True:
    response = requests.get(url)
    temperature = response.json()
    now = datetime.datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%Y-%m-%d %H:%M:%S")
    temperature['time'] = now
    print("Saving: " + json.dumps(temperature))
    db.temperatures.insert_one(temperature)
    time.sleep(5)