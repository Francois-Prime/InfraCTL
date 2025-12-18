import os

import click


def is_ci():
    return os.getenv("CI") == "true"

@click.Command
def apply():
    if is_ci():
        raise click.ClickException("Apply disabled in CI")