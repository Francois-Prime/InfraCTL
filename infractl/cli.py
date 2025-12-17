from random import choice

import click
import pathlib
import subprocess
import time
from pathlib import Path

@click.group()
def main():
    """Infractl CLI"""
    pass
@click.option('--env',
              required=True,
              type=click.Choice(['dev','qa','prod']),
              help="Load env")

@main.command()
def plan(env):
    """Print Plan"""
    infra_path = Path("infra")/ env
    ## verify = str(input(f"Executing 'terraform plan' in {infra_path}: do you want to continue? -- Type 'Y' or 'N'\n"))

    if not infra_path.exists() or not infra_path.is_dir():
        click.echo(
            message='Error: Folder path does not exist: {infra_path}',
            err=True,
        )
        raise click.Abort()

    click.confirm(
        f"Executing 'terraform plan' in {infra_path}: Continue?",
        abort=True
    )

    click.echo(
        f'Planning infrastructure for env: {env}',
    )

    time.sleep(2)

    ## if verify == 'Y':
    result = subprocess.run(
        ["terraform", "plan"],
        cwd=infra_path,
    )

    if result != 0:
        raise click.Abort()
## else:
       ## raise click.Abort()

@main.command()
def stage():
    """Print Stage"""
    click.echo("Staging Changes")

@main.command()
def init():
    """Initialize plan"""
    click.echo("Init Changes")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
