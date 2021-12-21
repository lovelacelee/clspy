# -*- encoding: utf-8 -*-

import hashlib

class Md5(object):
    """wheel of md5
    """
    def __init__(self) -> None:
        super().__init__()

    def __repr__(self) -> str:
        return super().__repr__()

    def file(self, filename):
        '''
        :param filename: calc md5 digest from a file
        :return: md5 string
        '''
        m = hashlib.md5()
        with open(filename, 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                m.update(data)
        return m.hexdigest()

    def string(self, content):
        '''
        :param content: calc digest from string
        :return: md5 string
        '''
        m = hashlib.md5(content)
        return m.hexdigest()

    def same(self, f1, f2):
        '''
        :param f1: first filename or content<string>
        :param f2: second filename or content<string>
        :return: md5(f1) == md5(f2)
        '''
        if type(f1) == type(str) == type(f2):
            md51 = self.string(f1)
            md52 = self.string(f2)
        else:
            md51 = self.file(f1)
            md52 = self.file(f2)
        return md51 == md52