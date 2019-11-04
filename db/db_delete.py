import requests
import json
from sqlalchemy import delete
from db.sqlalchemydb import engine, locations_table, stations_table


def deleteLocationData(name):
    conn = engine.connect()
    d = delete(locations_table).where(locations_table.c.name == name)
    conn.execute(d)
    conn.close()

def deleteStationData(name):
    conn = engine.connect()
    d = delete(stations_table).where(stations_table.c.name == name)
    conn.execute(d)
    conn.close()