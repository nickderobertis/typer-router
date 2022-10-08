import typer

from tests.e2e.cli_stub import run_cli


def test_app_1_command_1_prints_a_b(app1_typer: typer.Typer):
    result = run_cli(app1_typer, "command1 --b 2 1")
    assert result.exit_code == 0
    assert result.stdout.strip() == "a=1, b=2"


def test_app_1_command_1_1_prints_e_f(app1_typer: typer.Typer):
    result = run_cli(app1_typer, "container1 command1_1 --f 2 1")
    assert result.exit_code == 0
    assert result.stdout.strip() == "e=1, f=2"


def test_app_1_command_1_2_prints_g_h(app1_typer: typer.Typer):
    result = run_cli(app1_typer, "container1 command1_2 --h 2 1")
    assert result.exit_code == 0
    assert result.stdout.strip() == "g=1, h=2"


def test_app_1_command_2_1_1_prints_c_d(app1_typer: typer.Typer):
    result = run_cli(app1_typer, "container2 container2_1 command2_1_1 --d 2 1")
    assert result.exit_code == 0
    assert result.stdout.strip() == "c=1, d=2"
