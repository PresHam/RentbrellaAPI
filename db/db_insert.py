from db.sqlalchemydb import locations_table, engine, stations_table


def insertLocation(name, address):
    conn = engine.connect()
    ins = locations_table.insert()
    new_location = ins.values(name=name,
                              address=address)
    conn.execute(new_location)
    conn.close()
    print('Location data inserted')

def insertStation(serial, premise_id, name):
    conn = engine.connect()
    ins = stations_table.insert()
    new_station = ins.values(serial=serial,
                             premise_id=premise_id,
                             name=name)
    conn.execute(new_station)
    conn.close()
    print('Station data inserted')