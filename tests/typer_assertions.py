from typing import Dict

import typer
from typer.models import TyperInfo


def assert_app1_typer_is_correct(typer_app: typer.Typer):
    assert typer_app.info.name == "app1"
    app_registered_groups = _registered_groups_dict(typer_app)
    app_registered_commands = _registered_commands_dict(typer_app)

    # Check container1.command1_1 and container1.command1_2
    assert "container1" in app_registered_groups
    container_1_group = app_registered_groups["container1"]
    container_1_commands = _registered_commands_dict(container_1_group.typer_instance)
    assert "command1_1" in container_1_commands
    assert "command1_2" in container_1_commands

    # Check container2.container2_1.command2_1_1
    assert "container2" in app_registered_groups
    container_2_group = app_registered_groups["container2"]
    container_2_registered_groups = _registered_groups_dict(
        container_2_group.typer_instance
    )
    assert "container2_1" in container_2_registered_groups
    container_2_1_group = container_2_registered_groups["container2_1"]
    container_2_1_commands = _registered_commands_dict(
        container_2_1_group.typer_instance
    )
    assert "command2_1_1" in container_2_1_commands

    # Check command1
    assert "command1" in app_registered_commands


def _registered_groups_dict(typer_app: typer.Typer) -> Dict[str, TyperInfo]:
    return {group.name: group for group in typer_app.registered_groups}


def _registered_commands_dict(typer_app: typer.Typer) -> Dict[str, TyperInfo]:
    return {command.name: command for command in typer_app.registered_commands}
