import typer


def main(g: str = typer.Argument(...), h: str = typer.Option("h")):
    typer.echo(f"g={g}, h={h}")
