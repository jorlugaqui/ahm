from flask import current_app as app
from flask_restful import Resource, abort, reqparse
from flasgger import swag_from

from models import Measurement, User, Report
from utils import normalize_data, get_today_date, get_formatted_date


class AHMResource(Resource):
    def __init__(self, field_required=True):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('sys', type=int, required=field_required, location='json')
        self.reqparse.add_argument('dia', type=int, required=field_required, location='json')
        self.reqparse.add_argument('pul', type=int, required=field_required, location='json')
        super().__init__()

    def abort_with_http_code_error(self, code, message):
        app.logger.info(message)
        abort(code, message=message)


class MeasurementDetail(AHMResource):
    def __init__(self):
        super().__init__(field_required=False)

    @swag_from('docs/measurement_get.yml', methods=['GET'])
    def get(self, id):
        """
        Returns a measurement given its ID
        """
        measurement = Measurement.objects(id=id).first()
        if measurement is not None:
            return measurement.to_dict(), 200
        self.abort_with_http_code_error(404, f'Measurement ID={id} was not found')

    @swag_from('docs/measurement_update.yml', methods=['PUT'])
    def put(self, id):
        """
        Updates a measurement given its ID
        """
        measurement = Measurement.objects(id=id).first()
        if measurement is not None:
            if get_formatted_date(get_today_date()) != get_formatted_date(measurement.created):
                self.abort_with_http_code_error(
                    400, f'Cannot update a measurement for {get_formatted_date(measurement.created)}'
                )
            data = self.reqparse.parse_args()
            data = normalize_data(data)
            if not data:
                self.abort_with_http_code_error(
                    400, 'Payload cannot be empty'
                )
            measurement.update(**data)
            measurement.reload()
            return measurement.to_dict(), 200
        self.abort_with_http_code_error(404, f'Measurement ID={id} was not found')


class MeasurementList(AHMResource):
    def __init__(self):
        super().__init__(field_required=True)

    @swag_from('docs/measurement_list.yml', methods=['GET'])
    def get(self):
        """
        Get all measurements
        """
        data = [measurement.to_dict() for measurement in Measurement.latest()] # pylint: disable=no-value-for-parameter
        return data, 200

    @swag_from('docs/measurement_create.yml', methods=['POST'])
    def post(self):
        """
        Creates a measurement
        """
        data = self.reqparse.parse_args()
        measurement = Measurement(**data)
        user = User.objects(email='jorlugaqui@gmail.com').modify(
            upsert=True,
            new=True,
            set__email='jorlugaqui@gmail.com',
            set__name='Jorge',
            set__surname='Galvis'
        )
        measurement.user = user
        measurement.save()
        return measurement.to_dict(), 201


class ReportDetail(AHMResource):
    @swag_from('docs/report_detail.yml', methods=['GET'])
    def get(self, period):
        """
        Returns a list of measurements given a time-period range
        """
        report = Report.objects(period=period).first()
        if report is not None:
            return report.to_dict(), 200
        self.abort_with_http_code_error(404, f'Report con period={period} was not found')
