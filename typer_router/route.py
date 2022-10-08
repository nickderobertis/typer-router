from pathlib import Path
from typing import List

from pydantic import BaseModel

from typer_router.exc import NoParentRouteException

DEFAULT_FUNCTION_NAME = "main"


class Route(BaseModel):
    import_path: str
    name: str
    is_dir: bool
    function_name: str = DEFAULT_FUNCTION_NAME

    @property
    def parts(self) -> List[str]:
        return self.import_path.split(".")

    @property
    def subpaths(self) -> List[str]:
        parts = self.parts
        return [".".join(parts[:i]) for i in range(1, len(parts))]

    @property
    def subroutes(self) -> List["Route"]:
        return [
            Route.from_import_path(path, is_dir=True, function_name=self.function_name)
            for path in self.subpaths
        ]

    @property
    def parent(self) -> "Route":
        try:
            return self.subroutes[-1]
        except IndexError:
            raise NoParentRouteException(f"No parent route for {self.import_path}")

    @property
    def depth(self) -> int:
        return len(self.parts)

    @classmethod
    def from_file_path(
        cls, file_path: Path, function_name: str = DEFAULT_FUNCTION_NAME
    ) -> "Route":
        import_path = file_path.as_posix().replace("/", ".").replace(".py", "")
        name = file_path.stem
        return cls(
            import_path=import_path,
            name=name,
            is_dir=False,
            function_name=function_name,
        )

    @classmethod
    def from_import_path(
        cls, import_path: str, is_dir: bool, function_name: str = DEFAULT_FUNCTION_NAME
    ) -> "Route":
        name = import_path.split(".")[-1]
        return cls(
            import_path=import_path,
            name=name,
            is_dir=is_dir,
            function_name=function_name,
        )
