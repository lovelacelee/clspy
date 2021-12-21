# -*- encoding: utf-8 -*-


def clspy_singleton(cls, *args, **kv):
    """ Wrapper function to construct a singleton

    :return: a singleton class
    :rtype: object
    """
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls(*args, **kv)
        return _instance[cls]

    return inner


class SingletonClass(object):
    """ Singleton class wapper
    Only support **__init__** function without parameters, usage:

    class Cls(SingletonClass):
        def __init__(self):
            pass

    """
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(SingletonClass, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class SingletonMetaclass(type):
    """Metaclass implement, usage:

    class Cls(metaclass=SingletonMetaclass):
        pass
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMetaclass,
                                        cls).__call__(*args, **kwargs)
        return cls._instances[cls]


"""
Some other singleton class implement method
#--------------------------------------------------------------------
# Use __new__
#--------------------------------------------------------------------
class Single(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance
    def __init__(self):
        pass
"""
