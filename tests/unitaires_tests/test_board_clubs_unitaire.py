from Python_Testing import server


def test_board_clubs_valid_url(client):
    response = client.get("/boardClubs")
    assert response.status_code == 200


def test_board_clubs_valid_render_template(mocker, client, captured_templates):
    fake_clubs = [{
        "name": "le club fake 1",
        "email": "jj@simplylift.co",
        "points": "24"
    }]
    mocker_club = mocker.patch.object(server, 'clubs', fake_clubs)
    response = client.get("/boardClubs")
    data = response.data.decode()
    template, context = captured_templates[0]
    assert template.name == "boardclub.html"
    assert context["clubs"] == fake_clubs
    assert fake_clubs[0]['name'] in data
    assert fake_clubs[0]['points'] in data


