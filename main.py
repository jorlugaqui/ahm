import constants
from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flasgger import Swagger

from resources import MeasurementList, MeasurementDetail, ReportDetail

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': constants.DB_HOST,
    'db': constants.DB_NAME,
    'connect': False,
    'username': constants.DB_USER,
    'password': constants.DB_PASSWORD,
    'authentication_source': 'admin'
}

app.config['SWAGGER'] = {
    'title': 'AHM API',
    'uiversion': 2
}

api = Api(app, catch_all_404s=True)
db = MongoEngine(app)
swagger = Swagger(app)

api.add_resource(MeasurementDetail, '/v1/measurements/<string:id>')
api.add_resource(MeasurementList, '/v1/measurements')
api.add_resource(ReportDetail, '/v1/report/<string:period>')


if __name__ == '__main__':
    app.run(host=constants.API_HOST)
