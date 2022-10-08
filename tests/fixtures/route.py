import pytest as pytest

from typer_router import Route

APP_1_IMPORT_PATH = "tests.input_files.app1"


@pytest.fixture
def app1_command1_route() -> Route:
    return Route.from_import_path("command1", is_dir=False)


@pytest.fixture
def app1_command1_1_route() -> Route:
    return Route.from_import_path("container1.command1_1", is_dir=False)


@pytest.fixture
def app1_command1_2_route() -> Route:
    return Route.from_import_path("container1.command1_2", is_dir=False)


@pytest.fixture
def app1_command2_1_1_route() -> Route:
    return Route.from_import_path("container2.container2_1.command2_1_1", is_dir=False)
