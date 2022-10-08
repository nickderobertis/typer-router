from typer_router import Router


def test_creates_typer_from_router(app1_router: Router):
    app1_router.to_typer()
