# -*- coding: utf-8 -*-
"""Main module."""
from os.path import dirname
import logging.config
import bottle
from pydbwrapper import Config

from services import *

#logging.config.fileConfig("{}/{}".format(dirname(__file__), 'logging.ini'))
logging.config.fileConfig("logging.ini")

Config.instance("config.json")
app = bottle.default_app()

if __name__ == "__main__":
    dev_options = {'host': '0.0.0.0', 'port': 8000,
                   'workers': 1, 'reload': True, 'debuging': True}
    bottle.run(**dev_options)
