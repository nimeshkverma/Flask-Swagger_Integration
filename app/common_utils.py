import json

from flask import Response


def get_header(token=None):
    header = {
        "X-VERSION-CODE": 18
    }
    if token:
        header["Authorization"] = token
    return header


def unauthorized_customer_error():
    body = {
        "s": 0,
        "m": "Token invalid!",
        "d": {},
    }
    response = Response(
        json.dumps(body), status=401, content_type='application/json')
    return response


def check_token(token, customerId=None):
    if token != None:
        return True
    else:
        return False


def invalid_input_error():
    body = {
        "s": 0,
        "m": "Invalid input!",
        "d": {}
    }
    response = Response(
        json.dumps(body), status=400, content_type='application/json')
    return response


def incorrect_input_fields_error():
    body = {
        "s": 0,
        "m": "Please enter correct input fields!",
        "d": {}
    }
    response = Response(
        json.dumps(body), status=200, content_type='application/json')
    return response


def no_data_found_error():
    body = {
        "s": 0,
        "m": "No data found!",
        "d": {}
    }
    response = Response(
        json.dumps(body), status=200, content_type='application/json')
    return response


def server_error():
    body = {
        "s": 0,
        "m": "Server issue. Please try again!",
        "d": {}
    }
    response = Response(
        json.dumps(body), status=500, content_type='application/json')
    return response


def get_success_response(s, m, d):
    body = {
        "s": s,
        "m": m,
        "d": d
    }
    response = Response(
        json.dumps(body), status=200, content_type='application/json')
    return response


def render_success_response(payload, status_code):
    response = Response(
        json.dumps(payload), status=status_code, content_type='application/json')
    return response


def regenerate_password(emailId):
    return True
