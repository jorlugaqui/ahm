import os
import json
import uuid

from datetime import datetime, timezone
from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)


API_HOST = os.environ.get('API_HOST', 'localhost')


def generate_uuid():
    identifier = uuid.uuid4()
    return json.dumps(identifier, default=str)


def get_utc_now():
    now = datetime.utcnow().replace(tzinfo=timezone.utc)
    return json.dumps(now, default=str)


MEASUREMENTS = [
    {
        'id': '840e0300-4ad7-4cf3-b0db-4f43eb883d26',
        'sys': 120,
        'dia': 80,
        'pul': 70,
        'created': get_utc_now(),
        'user_id': 'c0848663-1b9c-4a0b-a1e7-c1a783b4cb70'
    },
    {
        'id': '840e0300-4ad7-4cf3-b0db-4f43eb883d27',
        'sys': 170,
        'dia': 90,
        'pul': 70,
        'created': get_utc_now(),
        'user_id': 'c0848663-1b9c-4a0b-a1e7-c1a783b4cb71'
    }
]


class Measurement(Resource):
    def get(self, id):
        for measurement in MEASUREMENTS:
            if id == measurement.get('id'):
                return measurement, 200
        abort(404, message=f'Measurement ID={id} was not found')


class MeasurementList(Resource):
    def get(self):
        return MEASUREMENTS, 200

    def post(self):
        data = json.loads(request.data)
        measurement = {
            'id': generate_uuid(),
            'sys': data.get('sys'),
            'dia': data.get('dia'),
            'pul': data.get('pul'),
            'created': get_utc_now(),
            'user_id': 'c0848663-1b9c-4a0b-a1e7-c1a783b4cb71'
        }
        MEASUREMENTS.append(measurement)
        return measurement, 201


api.add_resource(Measurement, '/v1/measurements/<string:id>')
api.add_resource(MeasurementList, '/v1/measurements/')


if __name__ == '__main__':
    app.run(host=API_HOST)
