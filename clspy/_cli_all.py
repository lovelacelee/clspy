# -*- encoding: utf-8 -*-

import click
import clspy


@click.command(context_settings=dict(
    allow_extra_args=True,
    ignore_unknown_options=True,
),
               help="Show all exports of clspy.")
def all():

    click.secho(str(clspy.__all__), fg='green')
