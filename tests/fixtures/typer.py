import pytest
import typer

from typer_router import Router


@pytest.fixture
def app1_typer(app1_router: Router) -> typer.Typer:
    return app1_router.to_typer()
