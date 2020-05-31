from flask import current_app as app


def handle_db_request_exception(e):
    app.logger.error(e)
    return {'message': str(e)}, 400
