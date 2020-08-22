from flask import current_app as app


def handle_db_duplicate_error(e):
    app.logger.error(e)
    return {
        'message': 'A measurement for today was already added'
    }, 400


def handle_db_request_exception(e):
    app.logger.error(e)
    return {'message': str(e)}, 400


def handle_general_exception(e):
    app.logger.error(e)
    return {'message': str(e)}, 500
