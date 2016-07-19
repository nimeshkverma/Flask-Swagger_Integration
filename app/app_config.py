import os
import json
from flask import Flask, jsonify, request, Response
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler, SMTPHandler

app = Flask(__name__)


from app.v1.urls import v1

VERSION_OBJECT_MAPPING = {
    '1': v1,
}


def get_url_prefix(version):
    return '/' + str(version)


def register_versions(allowed_versions):
    for version in allowed_versions:
        app.register_blueprint(
            VERSION_OBJECT_MAPPING[version], url_prefix=get_url_prefix(version))


def configure_app(app):
    app.config.from_object("config.Config")
    FILE_LOGGER_CONFIG = app.config.get('FILE_LOGGER', {})
    file_handler = TimedRotatingFileHandler(FILE_LOGGER_CONFIG.get(
        'location'), when=FILE_LOGGER_CONFIG.get('duration'), backupCount=FILE_LOGGER_CONFIG.get('backup'))
    file_handler.setLevel(FILE_LOGGER_CONFIG.get('level'))
    file_handler.setFormatter(
        Formatter(FILE_LOGGER_CONFIG.get('format')))
    app.logger.addHandler(file_handler)


@app.errorhandler(404)
def page_not_found(e):
    body = {
        "s": 0,
        "m": "URL not supported!",
        "d": {}
    }
    return Response(
        json.dumps(body), status=404, content_type='application/json')


@app.errorhandler(405)
def page_not_found(e):
    body = {
        "s": 0,
        "m": "Method not allowed!",
        "d": {}
    }
    return Response(
        json.dumps(body), status=405, content_type='application/json')


@app.errorhandler(500)
def exception_handler(erro):
    body = {
        "s": 0,
        "m": "Server issue. Please try again!",
        "d": {}
    }
    return Response(
        json.dumps(body), status=500, content_type='application/json')


@app.before_request
def valid_json_request():
    if request.method == 'POST':
        body = {
            "s": 0,
            "m": "Invalid json",
            "d": {}
        }

        if request.headers.get('Content-Type') == 'application/json':
            try:
                request.get_json()
            except Exception as e:
                return Response(json.dumps(body), status=400, content_type='application/json')
        else:
            return Response(json.dumps(body), status=400, content_type='application/json')
