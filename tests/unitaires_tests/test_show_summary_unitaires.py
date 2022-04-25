from Python_Testing import server
from Python_Testing.server import formated_data


def test_show_summary_valide_email(mocker, client, captured_templates):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    valid_email = {"email": ["admin@irontemple.com"]}
    mocker.patch.object(server, 'clubs', fake_club)
    response = client.post("/showSummary", data=valid_email)
    assert len(valid_email["email"]) == 1
    assert response.status_code == 200
    data = response.data.decode()
    template, context = captured_templates[0]
    assert fake_club[0]['email'] == valid_email['email'][0]
    assert template.name == "welcome.html"
    assert '<p>Email non trouvé</p>' not in data
    assert "competitions" in context
    assert "club" in context


def test_show_summary_invalid_user(mocker, app, captured_templates):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    invalid_email = {"email": ""}
    with app.test_client() as client:
        mocker.patch.object(server, 'clubs', fake_club)
        response = client.post("/showSummary", data=invalid_email)
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "index.html"
        assert fake_club[0]['email'] != invalid_email['email']
        data = response.data.decode()
        assert '<p>Email non trouvé</p>' in data


def test_show_summary_not_allowed(client):
    response = client.get("/showSummary")
    assert response.status_code == 405


def test_show_summary_title_register(mocker, client):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    valid_email = {"email": ["admin@irontemple.com"]}
    mocker.patch.object(server, 'clubs', fake_club)
    response = client.post("/showSummary", data=valid_email)
    data = response.data.decode()
    name_db = fake_club[0]['name']
    assert f'<h2>Welcome, {name_db} </h2>' in data


def test_show_summary_point_register(mocker, client):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    valid_email = {"email": ["admin@irontemple.com"]}
    mocker.patch.object(server, 'clubs', fake_club)
    response = client.post("/showSummary", data=valid_email)
    data = response.data.decode()
    fake_club_point = fake_club[0]["points"]
    assert f'<p>Points available: {fake_club_point}</p>' in data


def test_book_valid_url_booking_display(mocker, client):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    valid_email = {"email": ["admin@irontemple.com"]}
    fake_competitions = [{'name': 'FakeCompetitionName', 'date': '2027-03-27 10:00:00', 'numberOfPlaces': '215'}]
    mocker.patch.object(server, 'competitions', fake_competitions)
    mocker.patch.object(server, 'clubs', fake_club)
    response = client.post("/showSummary", data=valid_email)
    data = response.data.decode()
    assert fake_competitions[0]['date'] > formated_data
    assert 'Book Places' in data


def test_show_summary_invalid_url_booking_display(mocker, client):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    fake_competitions = [{'name': 'Spring Festival', 'date': '2020-03-27 10:00:00', 'numberOfPlaces': '215'}]
    valid_email = {"email": ["admin@irontemple.com"]}
    mocker.patch.object(server, 'competitions', fake_competitions)
    mocker.patch.object(server, 'clubs', fake_club)
    response = client.post("/showSummary", data=valid_email)
    data = response.data.decode()
    assert fake_competitions[0]['date'] < formated_data
    assert 'Book Places' not in data
