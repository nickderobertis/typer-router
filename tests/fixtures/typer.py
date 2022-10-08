import pytest
import typer

from tests.fixtures import APP_1_IMPORT_PATH
from tests.input_files import app1 as app1_module
from typer_router import Router


@pytest.fixture
def app1_typer_manually_constructed(app1_router: Router) -> typer.Typer:
    return app1_router.to_typer(name="app1")


@pytest.fixture
def app1_typer_from_app_import_path() -> typer.Typer:
    app1_router = Router.from_app_import_path(APP_1_IMPORT_PATH)
    return app1_router.to_typer(name="app1")


@pytest.fixture
def app1_typer_from_app_module() -> typer.Typer:
    app1_router = Router.from_app_module(app1_module)
    return app1_router.to_typer(name="app1")


@pytest.fixture(
    params=[
        app1_typer_manually_constructed,
        app1_typer_from_app_import_path,
        app1_typer_from_app_module,
    ]
)
def app1_typer(request) -> typer.Typer:
    return request.getfixturevalue(request.param.__name__)
