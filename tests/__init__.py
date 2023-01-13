import os
from configparser import ConfigParser
TEST_INIT = os.path.abspath(__file__)
TEST_DIR = os.path.dirname(TEST_INIT)
PROJECT_PATH = os.path.dirname(TEST_DIR)

TEST_ENV= (os.environ.get('TEST_ENV'))


config = ConfigParser()
config.read(f'{PROJECT_PATH}/config.ini')

DOMAIN = config.get('TEST_ENV')







DOMAIN = 'http://hrm-online.portnov.com'
BASE_URL = f'{DOMAIN}/symfony/web/index.php'
DEFAULT_WAIT = 5
