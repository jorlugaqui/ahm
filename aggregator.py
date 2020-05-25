import os
import logging
from mongoengine import connect, disconnect
from models import Report, MeasurementValue, Measurement, User
from utils import get_yesterday_date, get_period, get_formatted_date

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
logger.addHandler(console)

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
            logger.error(e)
    return wrapper


@mongo_operation
def main():
    # Get current day - 1
    logger.info('Calculating yesterday\'s day')
    yesterday = get_yesterday_date()
    # Get yesterday's measurement
    logger.info(f'Getting measurement for {get_formatted_date(yesterday)}')
    measurement = Measurement.objects(created=get_formatted_date(yesterday)).first()
    if measurement is None:
        raise Exception(f'Measurement for date={get_formatted_date(yesterday)} was not found')

    logger.info(f'Calculating period for {get_formatted_date(yesterday)}')
    # Compute the period for that measurment
    period = get_period(yesterday)
    # Get the report by period
    logger.info(f'Getting report for {period}')
    report = Report.objects(period=period).first()
    if report is None:
        logger.info(f'Report not found, creating a new report for {period}')
        report = Report(
            period=period,
            values=[],
            user=User.objects(email='jorlugaqui@gmail.com').first()
        )
        report.save()

    logger.info(f'Adding a new measurement for {measurement.created} in period {period}')
    report_item = MeasurementValue(
        sys=measurement.sys,
        dia=measurement.dia,
        pul=measurement.pul,
        date=measurement.created,
        ok=measurement.is_ok()
    )
    report.values.append(report_item)
    report.save()
    logger.info(f'Done')


if __name__ == '__main__':
    main()
