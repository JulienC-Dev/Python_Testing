from Python_Testing import server
from Python_Testing.server import formated_data


def test_show_summary_valide_email(client, email):
    response = client.post("/showSummary", data=dict(email=email["email"][0]))
    assert len(email["email"]) == 1
    assert response.status_code == 200
    print(response.data)


def test_show_summary_not_allowed(client):
    response = client.get("/showSummary")
    assert response.status_code == 405


def test_show_summary_title_register(client, email, name):
    response = client.post("/showSummary", data=email)
    data = response.data.decode()
    name_db = name['name'][0]
    assert f'<h2>Welcome, {name_db} </h2>' in data


def test_show_summary_point_register(mocker, client, email):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    mocker.patch.object(server, 'clubs', fake_club)
    response = client.post("/showSummary", data=email)
    data = response.data.decode()
    fake_club_point = fake_club[0]["points"]
    assert f'<p>Points available: {fake_club_point}</p>' in data


def test_book_valid_url_booking_display(mocker, client, email):
    fake_competitions = [{'name': 'FakeCompetitionName', 'date': '2027-03-27 10:00:00', 'numberOfPlaces': '215'}]
    mocker.patch.object(server, 'competitions', fake_competitions)
    response = client.post("/showSummary", data=email)
    data = response.data.decode()
    assert fake_competitions[0]['date'] > formated_data
    assert 'Book Places' in data


def test_show_summary_invalid_url_booking_display(mocker, client, email):
    fake_competitions = [{'name': 'Spring Festival', 'date': '2020-03-27 10:00:00', 'numberOfPlaces': '215'}]
    mocker.patch.object(server, 'competitions', fake_competitions)
    response = client.post("/showSummary", data=email)
    data = response.data.decode()
    assert fake_competitions[0]['date'] < formated_data
    assert 'Book Places' not in data
