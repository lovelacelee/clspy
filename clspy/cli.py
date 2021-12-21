# -*- encoding: utf-8 -*-

import os
import click
from click.termui import prompt
from clspy import __version__

from clspy._cli_all import all

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(name="main", context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__, message='%(prog)s-%(version)s')
def main():
    """
    
    clspy is a set of fast programming tools that are gradually 
    generated during the python learning process.
    For more information, please contact [lovelacelee@gmail.com].
    Documents available on https://clspy.readthedocs.io/.
    WTFPL License Copyright (c) Connard Lee.
    """
    pass


main.add_command(all, name='all')

if __name__ == '__main__':
    main()
