import click



@click.group()
def main():
    """Infractl CLI"""
    pass

@main.command()
def plan():
    """Print Plan"""
    click.echo("Planning changes")

@main.command()
def stage():
    """Print Stage"""
    click.echo("Staging Changes")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
