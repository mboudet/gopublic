import click
from gopublic.cli import pass_context, json_loads
from gopublic.decorators import custom_exception, dict_output


@click.command('revoke')
@click.argument("token", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, token):
    """Revoke a token

Output:

    The API response
    """
    return ctx.gi.token.revoke(token)
