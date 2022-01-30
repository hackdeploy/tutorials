import os
from flask import Flask, jsonify,request
from flask_restful import Resource, Api, reqparse

from src.api import api

def get_app():
    app = Flask(__name__)
    api.init_app(app)


    @app.route('/')
    def home():
        print("home endpoint reached")

        return 'Hello docker!'

    return app

if __name__ == '__main__':
    app = get_app()
    app.run(host='0.0.0.0', port=5000)
    

    