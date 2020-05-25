import os

from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine

from resources import MeasurementList, MeasurementDetail

API_HOST = os.environ.get('API_HOST', 'localhost')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', '')
DB_USER = os.environ.get('DB_USER', '')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')

app = Flask(__name__)
api = Api(app, catch_all_404s=True)
db = MongoEngine()


app.config['MONGODB_SETTINGS'] = {
    'host': DB_HOST,
    'db': DB_NAME,
    'connect': False,
    'username': DB_USER,
    'password': DB_PASSWORD,
    'authentication_source': 'admin'
}
db.init_app(app)

api.add_resource(MeasurementDetail, '/v1/measurements/<string:id>')
api.add_resource(MeasurementList, '/v1/measurements')


if __name__ == '__main__':
    app.run(host=API_HOST)
