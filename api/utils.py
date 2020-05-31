from datetime import datetime, timedelta


def normalize_data(data):
    return {k: v for k, v in data.items() if v is not None}


def get_formatted_date(date):
    return datetime.strftime(date, '%Y-%m-%d')


def get_yesterday_date():
    return datetime.utcnow() - timedelta(1)


def get_today_date():
    return datetime.utcnow()


def get_period(date):
    if date.day < 16:
        return get_formatted_date(date.replace(day=15))

    last_day_of_month = get_last_day_of_month(date)
    return get_formatted_date(date.replace(day=last_day_of_month.day))


def get_last_day_of_month(date):
    next_month = date.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day)
