import json
from functools import wraps
from flask import request, Response
from jsonschema import validate, ValidationError, FormatChecker
from exception import ErrorMessage


def process_params(param_config=None, header_config=None, check_all_fields=True, *args, **kwargs):
    def deco(f):
        def incorrect_input_fields_error(msg):
            body = {
                "s": 0,
                "m": msg,
                "d": {}
            }
            response = Response(
                json.dumps(body), status=400, content_type='application/json')
            return response

        def extract_params(request):
            if request.method == 'POST':
                return request.get_json()
            else:
                return request.args

        def extract_headers(headers, config):
            required_header = {}
            all_present = True
            if config:
                for header_name, header_type in config.iteritems():
                    required_header[header_name] = headers(header_name)
                    if required_header[header_name]:
                        required_header[header_name] = header_type(
                            required_header[header_name])
                    else:
                        all_present = False
            return required_header, all_present

        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                params = extract_params(request)
                validate(params, param_config, format_checker=FormatChecker())
                if header_config:
                    header_params, all_params_present = extract_headers(
                        request.headers.get, header_config)
                    if not all_params_present:
                        return incorrect_input_fields_error("invalid headers")
                    return f(params=params, header_params=header_params, *args, **kwargs)
                else:
                    return f(params=params, *args, **kwargs)
            except ValidationError as e:
                return incorrect_input_fields_error(e.message)
        return decorated_function
    return deco


def authorization(f):
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

    def abstract_customerId(request):
        if request.method == 'POST':
            customerId = request.form.get(
                'customerId') or request.get_json().get("customerId")
        else:
            customerId = request.args.get('customerId')
        return customerId

    @wraps(f)
    def decorated_function(*args, **kwargs):
        customerId = abstract_customerId(request)
        token = request.headers.get("Authorization")
        if token:
            if customerId:
                if check_token(token, customerId):
                    return f(auth=True, *args, **kwargs)
        return unauthorized_customer_error()
    return decorated_function


def raise_exception(msg_prefix='', *args, **kwargs):
    def deco(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                msg = msg_prefix + str(e)
                raise ErrorMessage(msg)
        return decorated_function
    return deco
