import click
from builder import Builder


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())


@cli.command(help="run checker")
@click.argument('f', type=click.Path(exists=True), required=True)
def run(f):
    b = Builder(f)
    e = b.build()
    e.exec()

if __name__ == "__main__":
    cli()
