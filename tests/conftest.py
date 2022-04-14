import pytest
from Python_Testing import server


@pytest.fixture
def client():
    client = server.app
    return client.test_client()