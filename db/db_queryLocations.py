from db.sqlalchemydb import locations_table, engine
from sqlalchemy import select, column
import json


def selectLocations():
    conn = engine.connect()
    s = select([locations_table])
    result = conn.execute(s)
    result = result.fetchall()
    print(type(result))
    print(result)
    return result


selectLocations()