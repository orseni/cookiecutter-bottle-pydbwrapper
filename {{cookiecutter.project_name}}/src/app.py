# -*- coding: utf-8 -*-
"""Main module."""
import logging.config
import os
import simplejson
import datetime

import bottle
#from auth.autorizacao import before_request
from pydbwrapper import Config
from services import *


class CustomEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return str(obj.strftime("%Y-%m-%d %H:%M:%S"))
        return simplejson.JSONEncoder.default(self, obj)


def registra_plugins():
    from bottle_cerberus import CerberusPlugin
    bottle.install(CerberusPlugin())
    bottle.install(bottle.JSONPlugin(json_dumps=lambda s: simplejson.dumps(s, cls=CustomEncoder)))


def init_database():
    Config.instance("database.json")


def config_logging():
    currentdir = os.path.dirname(__file__)
    logging_config_file = os.path.join(currentdir, "logging.ini")
    logging.config.fileConfig(logging_config_file)


def build_app(debug=False):
    bottle.debug(debug)
    bottle.BaseRequest.MEMFILE_MAX = (1024 * 1024) * 4
    registra_plugins()
    init_database()
    app = bottle.default_app()
    # descomente essa linha para ligar a segurança de serviços por JWT
    # app.add_hook('before_request', before_request)
    return app


debug = os.getenv('BOTTLE_DEBUG', True)
app = build_app(debug)

if __name__ == "__main__":
    dev_options = {
        'host': os.getenv('BOTTLE_HOST', '0.0.0.0'),
        'port': os.getenv('BOTTLE_PORT', 8000),
        'workers': os.getenv('BOTTLE_QTD', 1),
        'reload': os.getenv('BOTTLE_RELOAD', True),
        'debug': debug
    }

    bottle.run(**dev_options)
