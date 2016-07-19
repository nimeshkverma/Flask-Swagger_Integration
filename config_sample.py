from logging import ERROR, CRITICAL


class Config(object):
    DEBUG = True
    TESTING = False
    VERSIONS_ALLOWED = ['1']
    AGGREGATOR_URI = 'http://127.0.0.1:9000'
    FILE_LOGGER = {
        'format': '%(asctime)s %(levelname)s: %(message)s in %(pathname)s:%(funcName)s:%(lineno)d',
        'location': 'app.log',
        'level': ERROR,
        'duration': 'D',
        'backup': 30,

    }
    EMAIL_LOGGER = {
        'recipients': [''],
        'server': '',
        'sender': 'error@craftsvilla.com',
        'level': CRITICAL,
        'subject': 'Android App serving API failed!',
        'format': '''
    Message type:       %(levelname)s
    Location:           %(pathname)s:%(lineno)d
    Module:             %(module)s
    Function:           %(funcName)s
    Time:               %(asctime)s

    Message:            %(message)s
    '''
    }
