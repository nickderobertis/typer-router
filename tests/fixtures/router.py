import pytest

from tests.fixtures.route import *
from typer_router import Router


@pytest.fixture
def app1_router(
    app1_command1_route,
    app1_command1_1_route,
    app1_command1_2_route,
    app1_command2_1_1_route,
) -> Router:
    return Router(
        routes=[
            app1_command1_route,
            app1_command1_1_route,
            app1_command1_2_route,
            app1_command2_1_1_route,
        ],
        app_import_path=APP_1_IMPORT_PATH,
    )
