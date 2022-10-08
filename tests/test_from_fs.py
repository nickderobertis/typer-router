from tests.fixtures import APP_1_IMPORT_PATH
from tests.typer_assertions import assert_app1_typer_is_correct
from typer_router import Router


def test_creates_router_from_app_import_path():
    app1_router = Router.from_app_import_path(APP_1_IMPORT_PATH)


def test_typer_has_all_commands(app1_router: Router):
    app1_router = Router.from_app_import_path(APP_1_IMPORT_PATH)
    typer_app = app1_router.to_typer(name="app1")
    assert_app1_typer_is_correct(typer_app)
