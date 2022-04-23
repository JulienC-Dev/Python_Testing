
def test_route_summary_valid_user(app, email, captured_templates):
    with app.test_client() as client:
        response = client.post('/showSummary', data=email, follow_redirects=True)
        data = response.data.decode()
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "welcome.html"
        assert '<p>Email non trouvé</p>' not in data
        assert "competitions" in context
        assert "club" in context


def test_show_summary_invalid_user(app, email, captured_templates):
    invalid_email = {"email": ""}
    with app.test_client() as client:
        response = client.post("/showSummary", data=invalid_email)
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "index.html"
        assert email['email'] != invalid_email['email']
        data = response.data.decode()
        assert '<p>Email non trouvé</p>' in data



