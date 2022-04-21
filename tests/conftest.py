import pytest
from Python_Testing import server
from flask import template_rendered


@pytest.fixture
def client():
    client = server.app
    return client.test_client()


@pytest.fixture
def email():
    email = {"email": ["admin@irontemple.com"]}
    return email


@pytest.fixture
def name():
    name = {"name": ["Iron Temple"]}
    return name


@pytest.fixture
def point():
    point = {"point": ["4"]}
    return point


@pytest.fixture
def name_competion():
    name_competion = {"name": ["Spring Festival"]}
    return name_competion

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

