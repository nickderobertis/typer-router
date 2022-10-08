import importlib
from typing import TYPE_CHECKING, Dict, Set

import typer

from typer_router.exc import NoParentRouteException

if TYPE_CHECKING:
    from typer_router.route import Route
    from typer_router.router import Router

TyperDict = Dict[str, typer.Typer]


def create_typer_app_from_router(router: "Router", **typer_kwargs) -> typer.Typer:
    app = typer.Typer(**typer_kwargs)
    nested_apps: TyperDict = {}

    for route in router.routes:
        # Handle the parents of the leaf nodes, as those will just be container typers
        try:
            parent = route.parent
        except NoParentRouteException:
            parent = None

        if parent:
            container_typer = nested_apps.get(parent.import_path)
            if container_typer is None:
                container_typer = typer.Typer(name=parent.name)
                nested_apps[parent.import_path] = container_typer
            # Connect the leaf node to the container
            add_route_to_typer_app(route, router, container_typer)
        else:
            # This is a root command, add directly to main typer
            add_route_to_typer_app(route, router, app)

    # Now create the nested container typers to fill in the gaps.
    # For example, if we have the following routes:
    #  - a.b.c.d
    #  - a.b.f.g
    #  - a.b.h.i.j
    # Then c, d, f, g, i, and j have already been created but b and h still need to be created.
    for route in router.routes:
        for sub_route in route.subroutes:
            path = sub_route.import_path
            if path not in nested_apps:
                container_typer = typer.Typer(name=sub_route.name)
                nested_apps[path] = container_typer
                # app.add_typer(container_typer, name=sub_route.name)

    # Now one last pass to connect all the typers together.
    # The leaf nodes and their containers are already connected
    # But we need to connect any intermediate containers and also connect
    # the top level containers to the main app.
    # For example, if we have the following routes:
    #  - a.b.c.d
    #  - a.b.f.g
    #  - a.b.h.i.j
    #  - a.k
    # We now need to connect b to a, k to a, and h to b.
    # This will make more sense after reading the prior block of comments
    already_connected: Set[str] = {route.import_path for route in router.routes}
    # Start from connecting to the main app
    for route in router.routes:
        # Need to create from leaf inwards so that commands will exist when connecting to main app
        for sub_route in reversed(route.subroutes):
            # E.g. for sub_route:
            # a.b.c.d we will get a.b.c, a.b, a
            # a.b.h.i.j we will get a.b.h.i, a.b.h, a.b, a
            # a.k we will get a
            if sub_route.import_path in already_connected:
                continue
            app_to_connect = nested_apps[sub_route.import_path]
            try:
                parent_app = nested_apps[sub_route.parent.import_path]
            except NoParentRouteException:
                parent_app = app
            parent_app.add_typer(app_to_connect, name=sub_route.name)
            already_connected.add(sub_route.import_path)

    return app


def add_route_to_typer_app(route: "Route", router: "Router", app: typer.Typer):
    # Load the python file from the route's import path
    # and get the route's function from the file
    full_import_path = router.full_import_path_for(route)
    module = importlib.import_module(full_import_path)
    func = getattr(module, route.function_name)

    app.command(route.name)(func)
