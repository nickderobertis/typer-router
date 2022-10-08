import typer


def main(c: str = typer.Argument(...), d: str = typer.Option("d")):
    typer.echo(f"c={c}, d={d}")
