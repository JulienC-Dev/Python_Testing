from flask import url_for
from Python_Testing import server


def test_book_valid_data_url(mocker, client, app):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    fake_competitions = [{'name': 'Spring Festival', 'date': '2020-03-27 10:00:00', 'numberOfPlaces': '215'}]
    club_valid_name = fake_club[0]['name']
    competition_valid_name = fake_competitions[0]['name']
    with client:
        with app.app_context():
            mocker.patch.object(server, 'competitions', fake_competitions)
            mocker.patch.object(server, 'clubs', fake_club)
            assert client.get(url_for('book', club=club_valid_name, competition=competition_valid_name)).status_code == 200


def test_book_invalid_data_url(mocker, client, app):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    fake_competitions = [{'name': 'Spring Festival', 'date': '2020-03-27 10:00:00', 'numberOfPlaces': '215'}]
    name_competion = "invalid Name competition"
    name = "invalid Name club"
    with client:
        with app.app_context():
            mocker.patch.object(server, 'competitions', fake_competitions)
            mocker.patch.object(server, 'clubs', fake_club)
            res = client.get(url_for('book', club=name, competition=name_competion), follow_redirects=True)
            data = res.data.decode()
            assert '<li>Something went wrong-please try again</li>' in data
            assert res.status_code == 200