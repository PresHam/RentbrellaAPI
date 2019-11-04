from db.sqlalchemydb import locations_table, engine, stations_table
from sqlalchemy import select, column
import json


def selectLocation(name):
    conn = engine.connect()
    s = select([locations_table]).where(locations_table.c.name == name)
    result = conn.execute(s)
    result = result.fetchall()
    conn.close()
    return result

def selectStation(name):
    conn = engine.connect()
    s = select([stations_table]).where(stations_table.c.name == name)
    result = conn.execute(s)
    result = result.fetchall()
    conn.close()
    return result

def selectLocations():
    conn = engine.connect()
    s = select([locations_table])
    result = conn.execute(s)
    result = result.fetchall()
    conn.close()
    return result

def selectStations(premise_id):
    conn = engine.connect()
    s = select([stations_table]).where(stations_table.c.premise_id == premise_id)
    result = conn.execute(s)
    result = result.fetchall()
    conn.close()
    return result