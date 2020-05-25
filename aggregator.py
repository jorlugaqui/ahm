import os
from mongoengine import connect, disconnect
from models import Report, MeasurementValue, Measurement, User
from utils import get_yesterday_date, get_period, get_formatted_date

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', '')
DB_USER = os.environ.get('DB_USER', '')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')


def mongo_operation(func):
    def wrapper():
        try:
            connect(DB_NAME, host=DB_HOST, username=DB_USER, password=DB_PASSWORD, authentication_source='admin')
            func()
            disconnect(alias=DB_NAME)
        except Exception as e:
            print(e)
    return wrapper


@mongo_operation
def main():
    # Get current day - 1
    yesterday = get_yesterday_date()
    # Get yesterday's measurement
    measurement = Measurement.objects(created=get_formatted_date(yesterday)).first()
    if measurement is None:
        raise Exception(f'Measurement for date={yesterday} was not found')

    # Compute the period for that measurment
    period = get_period(yesterday)
    # Get the report by period
    report = Report.objects(period=period).first()
    if report is None:
        report = Report(
            period=period,
            values=[],
            user=User.objects(email='jorlugaqui@gmail.com').first()
        )
        report.save()

    report_item = MeasurementValue(
        sys=measurement.sys,
        dia=measurement.dia,
        pul=measurement.pul,
        date=measurement.created,
        ok=measurement.is_ok()
    )
    report.values.append(report_item)
    report.save()


if __name__ == '__main__':
    main()
