# -*- encoding: utf-8 -*-

from .version import clspy_Version

from .config import Config, ConfigType, ConfigUnique

from .singleton import clspy_singleton
from .singleton import SingletonClass
from .singleton import SingletonMetaclass

from .crypto import Md5

from .log import Logger

from .db import Sql

from .utils import *

__all__ = [
    'Config', 'ConfigType', 'ConfigUnique', 'clspy_singleton',
    'SingletonClass', 'SingletonMetaclass', 'Md5', 'Logger', 'Sql'
]

__version__ = clspy_Version
"""Logger wapper"""
__clslq_log = Logger()
clslog = __clslq_log.log
