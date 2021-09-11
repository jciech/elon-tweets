from app import create_app
from unittest import mock


def mock_load_secrets(*args, **kwargs):
    return {}


def test_create_app():
    with mock.patch("app.app.load_secrets", mock_load_secrets):
        app = create_app()
        assert app is not None
