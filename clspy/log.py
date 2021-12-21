# -*- encoding: utf-8 -*-

import sys
import logging
from logging import critical, handlers, info
from .singleton import SingletonClass
from .utils import mkdir_p


class Logger(SingletonClass):
    """Gloable logging wrapper

    This class inherits a module named loguru, Logger module will use pure logging
    if loguru module not imported correctly.

    """
    _logfile = None
    _filehdr = None
    _loglevel = logging.DEBUG
    _root_logger = logging.RootLogger(logging.DEBUG)
    _fmtstring = '[%(levelname)-8.8s %(asctime)s %(filename)s:%(lineno)d] %(message)s'

    def __init__(self, file=None) -> None:
        super().__init__()
        self._logfile = file
        self._root_logger.handlers.clear()
        '''Console'''
        console = logging.StreamHandler()
        console.setLevel(self._loglevel)
        console.setFormatter(logging.Formatter(self._fmtstring))
        self._root_logger.addHandler(console)
        """
        Instance of TimedRotatingFileHandler
        interval: interval
        backupCount: delete log file more then backupCount files
        when: S-Seconds M-Miniutes H-Hours D-Days W-Weeks(==0 means monday) midnight(00:00)
        """
        if self._logfile:
            mkdir_p(self._logfile)
            self._filehdr = handlers.TimedRotatingFileHandler(self._logfile,
                                                              backupCount=3,
                                                              when='D',
                                                              encoding='utf-8')
            self._filehdr.setFormatter(logging.Formatter(self._fmtstring))
            self._filehdr.setLevel(self._loglevel)
            self._root_logger.addHandler(self._filehdr)

    @property
    def log(self, filename=None):
        """get a logger

        Args:
            filename (Path, optional): Log to file. Defaults to None.

        Returns:
            logger: <loguru.logger> returns if loguru imported correctly, otherwise
            <root_logger> returns
        """
        try:
            '''pip install logru'''
            from loguru import logger
            if filename:
                logger.add(
                    "logs/app.log",
                    rotation="2 days",
                    retention="14",
                    format=
                    '[{time:YYYY-MM-DD HH:mm:ss} |{level:8.8s}| {file}:{line}]{message}',
                    encoding='utf-8',
                    enqueue=True)
            logger.add(
                sys.stderr,
                format=
                '[<green>{time:YYYY-MM-DD HH:mm:ss}</green> |{level:8.8s}| {file}:<green>{line}</green>]{message}',
                encoding='utf-8',
                enqueue=True,
                colorize=True)
            return logger
        except:
            return Logger._root_logger

    @property
    def file(self):
        return self._logfile

    @file.setter
    def file(self, path):
        self._logfile = path
