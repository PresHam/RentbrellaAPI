from flask import Flask, request
from flask_restful import Resource, Api
from db.db_insert import *
from db.db_select import *
from solutions.list2json import *


# Init app
app = Flask(__name__)
api = Api(app)

# Class to create and check locations
class Locations(Resource):
    #Create Location Endpoint
    def post(self):
        location_json = request.get_json()  # Receives body
        name = location_json['name']  # Uses fields name and address
        address = location_json['address']
        insertLocation(name, address)  # Insert json to database
        # Return location created with ID
        created_location = selectLocation(location_json['name'])
        query_location = {"id": created_location[0][0],
                          "name": created_location[0][1],
                          "address": created_location[0][2]}
        return query_location

    #Check created locations
    def get(self):
        listoflocations = selectLocations()
        json = list2json(listoflocations)
        return json

# Classe de stations
class Stations(Resource):
    # Create Stations Using
    def post(self):
        station_json = request.get_json()  # Receives body
        serial = station_json['serial']  # Uses fields name and address
        premise_id = station_json['premise_id']
        name = station_json['name']
        insertStation(serial, premise_id, name)  # Insert json to database
        # Return location created with ID
        created_station = selectStation(station_json['name'])
        query_station = {"serial": created_station[0][0],
                          "premise_id": created_station[0][1],
                          "name": created_station[0][2]}
        return query_station

# Classe de consulta stations por locations
class StationsList(Resource):
    def get(self, premise_id):
        listofstations = selectStations(premise_id)
        json = stationslist2json(listofstations)
        return json


# Configuração de Endpoints
api.add_resource(Locations, '/v1/premises')
api.add_resource(Stations, '/v1/stations')
api.add_resource(StationsList, '/v1/premises/<int:premise_id>/stations')


# Debug Condition
if __name__ == '__main__':
    app.run(debug=True)