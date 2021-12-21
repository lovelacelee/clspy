# -*- encoding: utf-8 -*-

import os
import sys
import json
import configparser
import traceback
from enum import Enum
from xml.etree import ElementTree as ET
from .singleton import SingletonMetaclass

try:
    '''pyyaml package is required'''
    import yaml
except Exception as e:
    traceback.format_exc()


class ConfigType(Enum):
    """Support types: Json, Yaml, Ini, Xml
    """
    CCJson = 1
    CCYaml = 2
    CCIni = 3
    CCXml = 4


class Config(object):
    """Config is a config manager

    Aim to support json/xml/ini/yaml parse and dump operations. 

    Object can be easily used ad python dict type.

    Json: object managed as dict

    Ini: object managed as dict

    Xml: ElementTree managed object

    Yaml: object managed as dict

    """
    _filepath = None
    _execpath = None
    _config = None
    _type = ConfigType.CCJson
    '''Only valid as xml config'''
    _tree = None

    def __init__(self, file="config.json") -> None:
        self._filepath = os.path.dirname(os.path.abspath(__file__))
        self._execpath = os.path.dirname(os.path.abspath(sys.argv[0]))
        sys.path.append(self._filepath)
        sys.path.append(self._execpath)
        self.load(file)

    def __repr__(self) -> str:
        return '<Config[{} @{}@{}] {}>'.format(self._type, self._filepath,
                                               self._execpath, self._config)

    def _guess_suffix(self, file):
        try:
            suffix = os.path.splitext(file)[-1]
        except:
            pass
        if suffix == '.json':
            return ConfigType.CCJson
        elif suffix == '.yaml':
            return ConfigType.CCYaml
        elif suffix == '.ini':
            return ConfigType.CCIni
        elif suffix == '.xml':
            return ConfigType.CCXml
        else:
            return None

    def get(self, key=None):
        """get config key from parsed contents

        Args:
            key (<str>, optional): key of value or object. Defaults to None.

        Returns:
            None
        """
        try:
            if self._type == ConfigType.CCXml:
                if key:
                    return self._config.find(key)
            elif self._type == ConfigType.CCJson or \
                    self._type == ConfigType.CCIni or \
                    self._type == ConfigType.CCYaml:
                return self._config[key]
            return self._config
        except Exception as e:
            # print("Config get '{}' failed[{}]".format(key, e))
            # traceback.print_exc()
            pass

    def load(self, file):
        """load config file

        Args:
            file: relative or absolute path to file

        Raises:
            Exception.args: Exception.args("Not supported")
        """
        self._type = self._guess_suffix(file)
        try:
            if self._type == ConfigType.CCIni:
                self._config = configparser.ConfigParser()
                self._config.read(file)
            elif self._type == ConfigType.CCXml:
                self._tree = ET.parse(file)
                self._config = self._tree.getroot()
            else:
                with open(file, 'r', encoding="utf-8") as fp:
                    if self._type == ConfigType.CCJson:
                        self._config = json.load(fp)
                    elif self._type == ConfigType.CCYaml:
                        fdata = fp.read()
                        self._config = yaml.safe_load(fdata)
                    else:
                        raise Exception.args("Not supported")
        except Exception as e:
            # print(e)
            pass
        finally:
            # print(self._config)
            pass

    def save(self, file):
        """dump config contents to file

        Args:
            file (Path): Where to dump file, path would be relative or absolute

        Raises:
            Exception.args: Exception.args("Not supported")

        Returns:
            False: If config content type is not match <file>'s suffix
        """
        savetype = self._guess_suffix(file)
        if self._type != savetype:
            return False
        try:
            if self._type == ConfigType.CCIni:
                self._config.write(file)
            elif self._type == ConfigType.CCXml:
                self._tree.write(file, encoding='utf-8', xml_declaration=True)
            else:
                with open(file, 'r', encoding="utf-8") as fp:
                    if self._type == ConfigType.CCJson:
                        json.dump(self._config, fp, indent=4)
                    elif self._type == ConfigType.CCYaml:
                        yaml.dump(self._config, file)
                    else:
                        raise Exception.args("Not supported")
        except Exception as e:
            # print(e)
            pass

class ConfigUnique(Config, metaclass=SingletonMetaclass):
    """Globally unique Config object

    Args:
        metaclass: Defaults to SingletonMetaclass.
    """
    pass