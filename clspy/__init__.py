# -*- encoding: utf-8 -*-

from .version import clspy_Version

from .config import Config, ConfigType

from .singleton import clspy_singleton
from .singleton import SingletonClass
from .singleton import SingletonMetaclass

__all__ = [
    'Config', 'ConfigType', 'clspy_singleton', 'SingletonClass',
    'SingletonMetaclass'
]

__version__ = clspy_Version
