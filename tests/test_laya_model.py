from app.core.laya_model import load_laya


def test_laya_loads():
    agent = load_laya()

    assert agent is not None


def test_app_imports():
    from app.main import app

    assert app is not None