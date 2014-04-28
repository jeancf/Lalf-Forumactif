# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger("lalf")

import os.path
import configparser

from lalf.exceptions import *

"""
Dictionnary containing the configuration
"""
config = {
    "url" : "",
    "admin_name" : "",
    "admin_password" : "",
    "table_prefix" : "",
    "use_ocr" : True,
    "gocr" : "",
    "verbose" : False
}

def read(filename):
    """
    Read the configuration from filename and write it in the config
    dictionnary
    """
    cfg = configparser.ConfigParser()
    with open(filename, "r") as f:
        cfg.read_file(f)

    try:
        for k,v in config.items():
            if type(v) == bool:
                config[k] = cfg.getboolean("Configuration", k)
            else:
                config[k] = cfg.get("Configuration", k)
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        raise InvalidConfigurationFile(filename, e)
