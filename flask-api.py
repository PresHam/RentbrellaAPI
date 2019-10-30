from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import os
from db_insert import insertLocation
from db_select import selectLocation


# Init app
app = Flask(__name__)
api = Api(app)


# Classe de locais
class Locations(Resource):
    def post(self):
        location_json = request.get_json()  # Receives body
        name = location_json['name']  # Uses fields name and address
        address = location_json['address']
        insertLocation(name, address)  # Insert json to database
        # Return location created with ID
        #created_location = selectLocation(location_json['name'])
        return location_json

'''
    def get(self):
        return()


# Classe de stations
class Stations(Resource):
    def post(self):
        return()

    def get(self):
        return()

# Classe de consulta stations por locations
class StationsList(Resource):
    def get(self):
        return()
'''


# Configuração de Endpoints
api.add_resource(Locations, '/v1/premises')
#api.add_resource(Stations, '/v1/stations')
#api.add_resource(StationsList, '/v1/premises/:premise_id/stations')

# Debug Condition
if __name__ == '__main__':
    app.run(debug=True)