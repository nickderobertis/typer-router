from typing import List

import typer
from pydantic import BaseModel

from typer_router.from_fs import routes_from_app_import_path
from typer_router.route import Route
from typer_router.to_typer import create_typer_app_from_router


class Router(BaseModel):
    routes: List[Route]
    app_import_path: str

    def to_typer(self, **typer_kwargs) -> typer.Typer:
        return create_typer_app_from_router(self, **typer_kwargs)

    def full_import_path_for(self, route: Route) -> str:
        return f"{self.app_import_path}.{route.import_path}"

    @classmethod
    def from_app_import_path(cls, app_import_path: str) -> "Router":
        routes = routes_from_app_import_path(app_import_path)

        return cls(routes=routes, app_import_path=app_import_path)
