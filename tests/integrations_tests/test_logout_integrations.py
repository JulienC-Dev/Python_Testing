import flask
from Python_Testing import server


def test_logout_route_without_connexion_user(app):
    with app.test_client() as client:
        response = client.get("/logout", follow_redirects=True)
        assert response.status_code == 200
        assert flask.request.path == "/"


def test_logout_route_connexion_user(mocker, app):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    fake_competitions = [{'name': 'Spring Festival', 'date': '2020-03-27 10:00:00', 'numberOfPlaces': '215'}]
    valid_email = {"email": "admin@irontemple.com"}
    with app.test_client() as client:
        mocker.patch.object(server, 'competitions', fake_competitions)
        mocker.patch.object(server, 'clubs', fake_club)
        response = client.post("/showSummary", data=valid_email)
        data = response.data.decode()
        assert response.status_code == 200
        name_db = fake_club[0]['name']
        assert f'<h2>Welcome, {name_db} </h2>' in data
        res_logout = client.get("/logout", follow_redirects=True)
        assert res_logout.status_code == 200
        assert flask.request.path == "/"