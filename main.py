import os

from datetime import date
from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from flask_mongoengine import MongoEngine
from mongoengine import Document, IntField, DateTimeField, StringField, \
    EmailField, ReferenceField
from mongoengine.errors import ValidationError, NotUniqueError
from werkzeug.exceptions import NotFound, BadRequest


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


class User(Document):
    email = EmailField(required=True)
    name = StringField(max_length=255, required=True)
    surname = StringField(max_length=255, required=True)


class Measurement(Document):
    sys = IntField(min_value=0, max_value=200, required=True)
    dia = IntField(min_value=0, max_value=200, required=True)
    pul = IntField(min_value=0, max_value=200, required=True)
    created = DateTimeField(default=date.today, unique=True)
    user = ReferenceField(User, required=True)

    def to_dict(self):
        return {
            'id': str(self.id),
            'sys': self.sys,
            'dia': self.dia,
            'pul': self.pul,
            'created': self.created.strftime("%Y-%m-%d"),
            'user': str(self.user.id)
        }


class MeasurementDetail(Resource):
    def get(self, id):
        try:
            measurement = Measurement.objects(id=id).first()
            if measurement is not None:
                return measurement.to_dict(), 200
            abort(404, message=f'Measurement ID={id} was not found')
        except NotFound as e:
            raise e
        except Exception as e:
            abort(500, message=str(e))


class MeasurementList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('sys', type=int, required=True, location='json')
        self.reqparse.add_argument('dia', type=int, required=True, location='json')
        self.reqparse.add_argument('pul', type=int, required=True, location='json')
        super(MeasurementList, self).__init__()

    def get(self):
        try:
            data = [measurement.to_dict() for measurement in Measurement.objects]
            return data, 200
        except Exception as e:
            abort(500, message=str(e))

    def post(self):
        try:
            data = self.reqparse.parse_args()
            measurement = Measurement(**data)
            user = User.objects(email='jorlugaqui@gmail.com').first()
            measurement.user = user
            measurement.save()
            return measurement.to_dict(), 201
        except BadRequest as e:
            abort(400, message=e.data.get('message'))
        except (NotUniqueError, ValidationError) as e:
            abort(400, message=str(e))
        except Exception as e:
            abort(500, message=str(e))


api.add_resource(MeasurementDetail, '/v1/measurements/<string:id>/')
api.add_resource(MeasurementList, '/v1/measurements/')


if __name__ == '__main__':
    app.run(host=API_HOST)
