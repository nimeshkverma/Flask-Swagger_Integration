from flask.views import View
from flask import request

import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../../')] + sys.path

from v1.decorators import authorization, process_params
from app.common_utils import render_success_response, get_success_response

header_config = {
    'with_auth': {
        "Authorization": str,
        "X-VERSION-CODE": int,
    },
    'without_auth': {
        "X-Session": str,
        "X-VERSION-CODE": str,
    }
}


class AddToMyCart(View):
    methods = ['POST']
    param_config = {
        'with_auth': {
            'type': 'object',
            'properties': {
                'customerId': {'type': 'string'},
                'productId': {'type': 'string'},
                'qty': {'type': 'number'}
            },
            'required': ['customerId', 'productId', 'qty']
        },
        'without_auth': {
            'type': 'object',
            'properties': {
                'productId': {'type': 'string'},
                'qty': {'type': 'number'}
            },
            'required': ['productId', 'qty']
        }
    }

    response_data = {
        "s": 1,
        "m": "Item sucessfully added to cart!",
        "d": {
            "products": [
                {
                    "regularPrice": 399,
                    "discountedPrice": 300,
                    "discountPercentage": 20,
                    "vendorDetails": {
                        "vendorId": "1",
                        "vendorCod": 1,
                        "vendorName": "Dola's Creation",
                        "vendorPincode": "400078"
                    },
                    "discountPercentage": 5,
                    "productName": "Work Intel Anklet",
                    "qty": 2,
                    "sellerNote": None,
                    "imgUrl": "/C/V/CV-MVISH51837745550-saree-Craftsvilla_1.jpg",
                    "productId": "1022"
                },
                {
                    "regularPrice": 699,
                    "discountedPrice": 400,
                    "discountPercentage": 20,
                    "vendorDetails": {
                        "vendorId": "1",
                        "vendorCod": 1,
                        "vendorName": "Dola's Creation",
                        "vendorPincode": "400078"
                    },
                    "discountPercentage": 0,
                    "productName": "Blue bage",
                    "qty": 1,
                    "sellerNote": None,
                    "imgUrl": "/C/V/CV-MVISH51837745550-bags-Craftsvilla_1.jpg",
                    "productId": "10282"
                }
            ],
            "orderSummary": {
                "totalPayable": 799,
                "couponDiscount": 0,
                "shippingCost": 0,
                "discount": 0,
                "total": 799,
                "subTotal": 799,
                "vat": 0
            }
        }
    }

    def dispatch_request(self):
        #@process_params(param_config=self.param_config['with_auth'], header_config=header_config['with_auth'])
        #@authorization
        def add_user_cart():
            print "inside auth"
            return render_success_response(self.response_data, 200)

        #@process_params(param_config=self.param_config['without_auth'], header_config=header_config['without_auth'])
        def add_guest_cart():
            print "inside guest"
            return render_success_response(self.response_data, 200)

        def perform():
            if request.headers.get("Authorization"):
                response = add_user_cart()
            else:
                response = add_guest_cart()
            print response
            return response

        return perform()


class MyCartDetails(View):
    methods = ['POST']
    param_config = {
        'with_auth': {
            'type': 'object',
            'properties': {
                'customerId': {'type': 'string'},
                'productId': {'type': 'string'},
                'qty': {'type': 'number'}
            },
            'required': ['customerId', 'productId', 'qty']
        },
        'without_auth': {
            'type': 'object',
            'properties': {
                'productId': {'type': 'string'},
                'qty': {'type': 'number'}
            },
            'required': ['productId', 'qty']
        }
    }

    response_data = {
        "s": 1,
        "m": "Item sucessfully added to cart!",
        "d": {
            "products": [
                {
                    "regularPrice": 399,
                    "discountedPrice": 300,
                    "discountPercentage": 20,
                    "vendorDetails": {
                        "vendorId": "1",
                        "vendorCod": 1,
                        "vendorName": "Dola's Creation",
                        "vendorPincode": "400078"
                    },
                    "discountPercentage": 5,
                    "productName": "Work Intel Anklet",
                    "qty": 2,
                    "sellerNote": None,
                    "imgUrl": "/C/V/CV-MVISH51837745550-saree-Craftsvilla_1.jpg",
                    "productId": "1022"
                },
                {
                    "regularPrice": 699,
                    "discountedPrice": 400,
                    "discountPercentage": 20,
                    "vendorDetails": {
                        "vendorId": "1",
                        "vendorCod": 1,
                        "vendorName": "Dola's Creation",
                        "vendorPincode": "400078"
                    },
                    "discountPercentage": 0,
                    "productName": "Blue bage",
                    "qty": 1,
                    "sellerNote": None,
                    "imgUrl": "/C/V/CV-MVISH51837745550-bags-Craftsvilla_1.jpg",
                    "productId": "10282"
                }
            ],
            "orderSummary": {
                "totalPayable": 799,
                "couponDiscount": 0,
                "shippingCost": 0,
                "discount": 0,
                "total": 799,
                "subTotal": 799,
                "vat": 0
            }
        }
    }

    def dispatch_request(self):
        @process_params(param_config=self.param_config['with_auth'], header_config=header_config['with_auth'])
        @authorization
        def add_user_cart(params, header_params, auth):
            print "inside auth"
            return render_success_response(self.response_data, 200)

        @process_params(param_config=self.param_config['without_auth'], header_config=header_config['without_auth'])
        def add_guest_cart(params, header_params):
            print "inside guest"
            return render_success_response(self.response_data, 200)

        def perform():
            if request.headers.get("Authorization"):
                response = add_user_cart()
            else:
                response = add_guest_cart()
            print response
            return response

        return perform()
