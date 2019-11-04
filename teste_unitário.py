import requests
import json
from sqlalchemy import delete
from db.sqlalchemydb import engine, locations_table
from db.db_delete import deleteLocationData, deleteStationData

print('\nBateria de testes\n')
## Creating location
try:
    url = 'http://127.0.0.1:5000/v1/premises'
    dados = {"name": 'GreenPeace',
         "address": 'Fradique Coutinho,352'
         }
    datajson = json.dumps(dados)
    answer = requests.post(url, json=dados)
    answer = json.loads(answer.text)
    print('[x]Location Created')
except:
    print("[ ]Location Created")

## Creating Stations
try:
    url = 'http://127.0.0.1:5000/v1/stations'
    dados = {"serial": '123456',
             "premise_id": 111,
             "name": 'Umbrella Corp'
         }
    datajson = json.dumps(dados)
    answer = requests.post(url, json=dados)
    answer = json.loads(answer.text)
    print('[x]Station Created')
except:
    print("[ ]Station Created")

## Getting location list
try:
    url = 'http://127.0.0.1:5000/v1/premises'
    answer = requests.get(url)
    print('[x]List of locations')
except:
    print('[ ]List of locations')


## Deleting created location
try:
    deleteLocationData('GreenPeace')
    deleteStationData('Umbrella Corp')
    print('[x]Test data deleted')
except:
    print('[ ]Test data deleted')