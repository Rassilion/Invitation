import os
import logging


class Config(object):
    SERVER_NAME='localhost:5000'
    # log
    LOG_LEVEL = logging.DEBUG
    SITE_NAME = 'Invation'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

