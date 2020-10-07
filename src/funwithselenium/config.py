from os import environ

TESTING = True
DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = environ.get('SECRET_KEY') #export SECRET_KEY='SqUiRtLe22' https://medium.com/@youngstone89/setting-up-environment-variables-in-mac-os-28e5941c771c
threaded=True
use_reloader=False