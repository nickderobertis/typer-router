from typing import List

import typer
from pydantic import BaseModel

from typer_router.route import Route
from typer_router.to_typer import create_typer_app_from_router


class Router(BaseModel):
    routes: List[Route]
    app_import_path: str

    def to_typer(self) -> typer.Typer:
        return create_typer_app_from_router(self)

    def full_import_path_for(self, route: Route) -> str:
        return f"{self.app_import_path}.{route.import_path}"
