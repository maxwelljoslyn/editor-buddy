import click


@click.command
@click.option("--laser", type=str, default="yellow")
def cli(laser):
    click.echo(f"You fired {laser} laser beams")
