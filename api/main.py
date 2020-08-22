from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flasgger import Swagger
from mongoengine.errors import ValidationError, NotUniqueError

import constants
import errors
from resources import MeasurementList, MeasurementDetail, ReportDetail

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': constants.DB_HOST,
    'db': constants.DB_NAME,
    'connect': False,
}

if not constants.CI:
    app.config['MONGODB_SETTINGS']['username'] = constants.DB_USER
    app.config['MONGODB_SETTINGS']['password'] = constants.DB_PASSWORD
    app.config['MONGODB_SETTINGS']['authentication_source'] = 'admin'

app.config['SWAGGER'] = {
    'title': 'AHM API',
    'uiversion': 3
}

CORS(app, resources={r'/*': {'origins': '*'}})

api = Api(app, catch_all_404s=True)
db = MongoEngine(app)
swagger = Swagger(app)


api.add_resource(MeasurementDetail, '/v1/measurements/<string:id>')
api.add_resource(MeasurementList, '/v1/measurements')
api.add_resource(ReportDetail, '/v1/report/<string:period>')

app.register_error_handler(ValidationError, errors.handle_db_request_exception)
app.register_error_handler(NotUniqueError, errors.handle_db_duplicate_error)
app.register_error_handler(Exception, errors.handle_general_exception)


if __name__ == '__main__':
    app.run(host=constants.API_HOST)
