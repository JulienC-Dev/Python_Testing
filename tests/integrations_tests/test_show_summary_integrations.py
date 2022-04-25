from Python_Testing import server


def test_route_summary_valid_user(mocker, app, captured_templates):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    valid_email = {"email": ["admin@irontemple.com"]}
    with app.test_client() as client:
        mocker.patch.object(server, 'clubs', fake_club)
        response = client.post('/showSummary', data=valid_email, follow_redirects=True)
        data = response.data.decode()
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert fake_club[0]['email'] == valid_email['email'][0]
        assert template.name == "welcome.html"
        assert '<p>Email non trouvé</p>' not in data
        assert "competitions" in context
        assert "club" in context


def test_show_summary_invalid_user(app, captured_templates):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    invalid_email = {"email": ""}
    with app.test_client() as client:
        response = client.post("/showSummary", data=invalid_email)
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "index.html"
        assert fake_club[0]['email'] != invalid_email['email']
        data = response.data.decode()
        assert '<p>Email non trouvé</p>' in data



