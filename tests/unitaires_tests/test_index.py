from Python_Testing import server

import pytest



def test_check_status_ok(client):
    response = client.get('/')
    assert response.status_code == 200


