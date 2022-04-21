def test_logout_check_status(app):
    with app.test_client() as client:
        response = client.get("/logout")
        assert response.status_code == 302

