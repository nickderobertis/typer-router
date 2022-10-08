from typing import Dict

import typer
from typer.models import TyperInfo

from tests.typer_assertions import assert_app1_typer_is_correct
from typer_router import Router


def test_creates_typer_from_router(app1_router: Router):
    app1_router.to_typer()


def test_typer_has_all_commands(app1_router: Router):
    typer_app = app1_router.to_typer(name="app1")
    assert_app1_typer_is_correct(typer_app)
