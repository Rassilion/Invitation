import os
import logging


class Config(object):
    # log
    LOG_LEVEL = logging.DEBUG
    SITE_NAME = 'Invation'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:////app.db'

