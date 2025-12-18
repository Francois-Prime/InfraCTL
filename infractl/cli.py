import click
import subprocess
import time
from infractl.utility import *
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

    if not infra_path.exists() or not infra_path.is_dir():
        click.echo(
            message='Error: Folder path does not exist: {infra_path}',
            err=True,
        )
        raise click.Abort()

    ''' 
    click.confirm(
        text=f"Executing 'terraform plan' in {infra_path}: Continue?",
        abort=True
    )
    '''

    if is_ci() == 'true':
        print(f"CI detected - skipping terraform execution")
        click.Abort()
        return

    else:
        click.echo(
            f"Executing 'terraform plan' in {infra_path}"
        )

        time.sleep(2)

        click.echo(
            f'Planning infrastructure for env: {env}',
        )

        time.sleep(2)

        result = subprocess.run(
            ["terraform", "plan"],
            cwd=infra_path,
        )

        if result != 0:
            raise click.Abort()

@main.command()
def apply():
    """Apply Terraform changes"""
    if is_ci() == 'true':
        raise click.ClickException("Apply disabled in CI")

    click.echo("Running terraform apply (local only)")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
