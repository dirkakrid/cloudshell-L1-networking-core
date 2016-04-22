__author__ = 'g8y3e'

import os
import sys
import json

from helper.system_helper import get_file_path

class ConfigurationParser:
    _CONFIG_JSON = None
    _CONFIG_PATH = "configuration/configuration.json"

    @staticmethod
    def init():
        configure_path = ConfigurationParser._CONFIG_PATH

        json_data = open(get_file_path(configure_path)).read()
        ConfigurationParser._CONFIG_JSON = json.loads(json_data)

    @staticmethod
    def get(*args):
        ConfigurationParser.init()

        result_data = ConfigurationParser._CONFIG_JSON
        for key in args:
            if key in result_data:
                result_data = result_data[key]
            else:
                return None

        return result_data
