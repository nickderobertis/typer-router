import typer


def main(e: str = typer.Argument(...), f: str = typer.Option("f")):
    typer.echo(f"e={e}, f={f}")
