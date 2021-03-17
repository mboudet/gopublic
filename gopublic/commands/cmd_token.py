import click
from gopublic.commands.token.create import cli as create
from gopublic.commands.token.revoke import cli as revoke


@click.group()
def cli():
    """
    Manipulate files managed by Gopublish
    """
    pass


cli.add_command(create)
cli.add_command(revoke)
