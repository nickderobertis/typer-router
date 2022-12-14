import importlib
from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from typer_router.route import Route


def routes_from_app_import_path(app_import_path: str) -> List["Route"]:
    """Create routes from an app import path."""
    app_path = _app_folder_from_import_path(app_import_path)
    return _routes_from_app_path(app_path)


def routes_from_app_module(app_module: ModuleType) -> List["Route"]:
    """Create routes from an app module."""
    app_path = _app_folder_from_app_module(app_module)
    return _routes_from_app_path(app_path)


def _routes_from_app_path(app_path: Path) -> List["Route"]:
    """Create routes from an app path."""
    from typer_router.route import Route

    # Iterate through nested directories and files
    routes: List[Route] = []
    for path in app_path.rglob("*"):
        if path.is_dir():
            continue
        if path.name == "__init__.py":
            continue
        if not path.name.endswith(".py"):
            continue
        relative_path = path.relative_to(app_path)
        route = Route.from_file_path(relative_path)
        routes.append(route)

    return routes


def _app_folder_from_import_path(app_import_path: str) -> Path:
    """Get the app folder from an app import path."""
    app_module = importlib.import_module(app_import_path)
    return _app_folder_from_app_module(app_module)


def _app_folder_from_app_module(app_module: ModuleType) -> Path:
    if app_module.__file__ is None:
        # Should not happen, for type narrowing
        raise ValueError(f"App module {app_module} has no __file__ attribute.")
    app_folder = Path(app_module.__file__).parent
    return app_folder
