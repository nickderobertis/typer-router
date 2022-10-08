from typing import Dict

import typer
from typer.models import TyperInfo

from typer_router import Router


def test_creates_typer_from_router(app1_router: Router):
    app1_router.to_typer()


def test_typer_has_all_commands(app1_router: Router):
    typer_app = app1_router.to_typer()
    app_registered_groups = _registered_groups_dict(typer_app)

    # Check container1.command1_1
    assert "container1" in app_registered_groups
    container_1_group = app_registered_groups["container1"]
    container_1_registered_groups = _registered_groups_dict(
        container_1_group.typer_instance
    )
    assert "command1_1" in container_1_registered_groups
    command_1_1_group = container_1_registered_groups["command1_1"]
    command_1_1_registered_commands = _registered_commands_dict(
        command_1_1_group.typer_instance
    )
    assert "main" in command_1_1_registered_commands

    # Check container2.container2_1.command2_1_1
    assert "container2" in app_registered_groups
    container_2_group = app_registered_groups["container2"]
    container_2_registered_groups = _registered_groups_dict(
        container_2_group.typer_instance
    )
    assert "container2_1" in container_2_registered_groups
    container_2_1_group = container_2_registered_groups["container2_1"]
    container_2_1_registered_groups = _registered_groups_dict(
        container_2_1_group.typer_instance
    )
    assert "command2_1_1" in container_2_1_registered_groups
    command_2_1_1_group = container_2_1_registered_groups["command2_1_1"]
    command_2_1_1_registered_commands = _registered_commands_dict(
        command_2_1_1_group.typer_instance
    )
    assert "main" in command_2_1_1_registered_commands

    # Check command1
    assert "command1" in app_registered_groups
    command_1_group = app_registered_groups["command1"]
    command_1_registered_commands = _registered_commands_dict(
        command_1_group.typer_instance
    )
    assert "main" in command_1_registered_commands


def _registered_groups_dict(typer_app: typer.Typer) -> Dict[str, TyperInfo]:
    return {group.name: group for group in typer_app.registered_groups}


def _registered_commands_dict(typer_app: typer.Typer) -> Dict[str, TyperInfo]:
    return {command.name: command for command in typer_app.registered_commands}
