import flask


def test_logout_route_without_connexion_user(app):
    with app.test_client() as client:
        response = client.get("/logout", follow_redirects=True)
        assert response.status_code == 200
        assert flask.request.path == "/"


def test_logout_route_connexion_user(app, email):
    with app.test_client() as client:
        response = client.post("/showSummary", data=email, follow_redirects=True)
        assert response.status_code == 200
        res_logout = client.get("/logout", follow_redirects=True)
        assert res_logout.status_code == 200
        assert flask.request.path == "/"