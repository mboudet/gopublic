import click
from gopublic.cli.cli import pass_context, json_loads
from gopublic.cli.decorators import custom_exception, dict_output


@click.command('create')
@click.argument("username", type=str)
@click.option(
    "--password",
    help="Optional password for library compatibility",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, username, password=""):
    """Get token

Output:

    Dictionnary containg the token
    """
    return ctx.gi.token.create(username, password=password)
