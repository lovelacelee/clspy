# -*- encoding: utf-8 -*-

import os
import sys
import platform
import re
import shutil
import click
from .crypto import Md5


def mkdir_p(absolute_path):
    """mkdir -p implement
    
    Usage: 
    
    mkdir_p('D:\\A\\B\\C.txt')

    mkdir_p('~/A/B/C')
    """
    path = os.path.dirname(absolute_path)
    if not os.path.exists(path):
        os.makedirs(path, 0o777)


def dir_copy(srcpath, dstpath):
    try:
        if not os.path.exists(srcpath):
            return
        if not os.path.exists(dstpath):
            if sys.version_info.major >= 3 and sys.version_info.minor >= 8:
                shutil.copytree(srcpath, dstpath, dirs_exist_ok=True)
            else:
                shutil.copytree(srcpath, dstpath)
    except Exception as e:
        pass


def rmdir(path):
    """
    Warning: all files and directories in path will be deleted.
    """
    if os.path.isfile(path):
        print("{} will be deleted.".format(path))
        os.remove(path)
        return
    for root, dirs, files in os.walk(path):
        for d in dirs:
            t = os.path.join(root, d)
            if os.path.exists(t):
                print("{} will be deleted.".format(t))
                shutil.rmtree(t)
        for f in files:
            t = os.path.join(root, f)
            if os.path.exists(path):
                print("{} will be deleted.".format(t))
                os.remove(t)


def win_runtime_cp(src, to):
    # useful while running a package by pyinstaller on windows
    if platform.system() == "Windows":
        for path in sys.path:
            if re.match(r'^_MEI\d+$', os.path.basename(path)):
                if os.path.exists(path):
                    dir_copy(src, to)
                    break


def is_frozen():
    # All of the modules are built-in to the interpreter, e.g., by py2exe
    return hasattr(sys, "frozen")


def pipguess():
    if platform.system() == "Windows":
        return "python -m pip "
    else:
        return "python3 -m pip "


def setenv(permanent=True, key=None, value=None):
    if permanent:
        """
        HERE is the way for permanently env-set under windows
        Administrator is required
        # with /m means system env
        # without /m means user env
        """
        systype = platform.system()
        if systype == "Windows":
            os.system(r"setx %s %s /m" % (key, value))
        else:
            os.environ['%s' % key] = value
    else:
        os.environ['%s' % key] = value


def pip_conf_install(src=None):
    try:
        if not src or not os.path.exists(src):
            src = os.path.join(os.path.dirname(__file__), 'pip.conf')
        systype = platform.system()
        if systype == "Windows":
            pipdotdir = os.path.join(os.getenv('APPDATA'), "pip")
            pip_dest = os.path.join(pipdotdir, "pip.ini")
        elif systype == "Darwin":
            pipdotdir = os.path.join(os.getenv('HOME'),
                                     "/Library/Application\ Support/pip/pip")
            pip_dest = os.path.join(pipdotdir, "pip.conf")
        else:
            pipdotdir = os.path.join(os.getenv('HOME'), ".pip")
            pip_dest = os.path.join(pipdotdir, "pip.conf")
        mkdir_p(pipdotdir)
        md5 = Md5()
        if os.path.exists(pip_dest) and md5.same(src, pip_dest):
            click.secho("{} exist already".format(pip_dest))
            return
        shutil.copyfile(src, pip_dest)
    except:
        pass
