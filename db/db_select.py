from db.sqlalchemydb import locations_table, engine
from sqlalchemy import select, column
import json


def selectLocation(name):
    conn = engine.connect()
    s = select([locations_table]).where(locations_table.c.name == name)
    result = conn.execute(s)
    result = result.fetchall()
    print(result)
    return result

selectLocation('Novos')