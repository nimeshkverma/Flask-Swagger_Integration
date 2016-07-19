import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from config import Config
from app_config import configure_app, register_versions, app

configure_app(app)
register_versions(Config.VERSIONS_ALLOWED)
