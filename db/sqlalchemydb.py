from datetime import date
from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String, DateTime)
import os


# Database Config
basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///locations.db', echo=False)

metadata = MetaData(bind=engine)

locations_table = Table('Locations', metadata,
                        Column('id', Integer, primary_key=True, index=True),
                        Column('name', String(100), unique=True),
                        Column('address', String(200))
                        )


stations_table = Table('Stations', metadata,
                       Column('serial', String(30)),
                       Column('premise_id', Integer, index=True),
                       Column('name', String(100), unique=True)
                      )

metadata.create_all()
