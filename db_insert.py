from sqlalchemydb import locations_table, engine


def insertLocation(name, address):
    conn = engine.connect()
    ins = locations_table.insert()
    new_location = ins.values(name=name,
                              address=address)

    conn.execute(new_location)
    print('Dados Inseridos')