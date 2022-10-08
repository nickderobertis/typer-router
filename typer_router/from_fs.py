from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from typer_router.route import Route


def routes_from_app_import_path(app_import_path: str) -> List["Route"]:
    """Create routes from an app import path."""

    return []
