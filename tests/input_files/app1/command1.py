import typer


def main(a: str = typer.Argument(...), b: str = typer.Option("b")):
    typer.echo(f"a={a}, b={b}")
