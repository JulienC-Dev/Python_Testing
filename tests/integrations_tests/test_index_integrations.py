

def test_index_route_login_page_to_welcome_page(mocker, client):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    valid_email = {"email": ["admin@irontemple.com"]}
    response = client.get("/", follow_redirects=True)
    assert response.status_code == 200
    mocker.patch.object(server, 'clubs', fake_club)
    res = client.post("/showSummary", data=valid_email, follow_redirects=True)
    data = res.data.decode()
    assert res.status_code == 200
    fake_club_name = fake_club[0]['name']
    assert f'<h2>Welcome, {fake_club_name} </h2>' in data

