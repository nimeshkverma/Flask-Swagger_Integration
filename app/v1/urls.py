from flask import Blueprint
from cart import views as cart_views
v1 = Blueprint('v1', __name__)

CACHED_PREFIX = '/public'
NON_CACHED_PREFIX = '/personal'


# cart urls
carts_public_prefix = CACHED_PREFIX + '/cart'
carts_private_prefix = NON_CACHED_PREFIX + '/cart'

v1.add_url_rule(carts_private_prefix + '/addToMyCart',
                view_func=cart_views.AddToMyCart.as_view('add_to_my_cart'))
