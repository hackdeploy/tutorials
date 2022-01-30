from os import utime
from flask import jsonify
from flask_restful import Api, Resource

api = Api(prefix="/api")

#data processing endpoint
#api.add_resource(health_check,'/health/')#Get