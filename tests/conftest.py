import pytest
from Python_Testing import server
from flask import template_rendered


@pytest.fixture
def client():
    client = server.app
    return client.test_client()


@pytest.fixture
def app():
    client = server.app
    return client


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

