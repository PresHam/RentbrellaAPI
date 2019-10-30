from sqlalchemydb import locations_table, engine
from sqlalchemy import select, column
import json

def selectLocation(name):
    conn = engine.connect()
    name = "name is equal DANILO"
    sel = select([locations_table]).where('name' == 1)
    result = conn.execute(sel)
    result = result.fetchall()
    print(type(result))
    print(result)
    print(sel)

selectLocation("Danilo")
