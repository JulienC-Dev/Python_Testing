
def test_show_summary_valide_email(client, email):
    response = client.post("/showSummary", data=dict(email=email["email"][0]))
    assert len(email["email"]) == 1
    assert response.status_code == 200


def test_show_summary_not_allowed(client):
    response = client.get("/showSummary")
    assert response.status_code == 405


def test_show_summary_title_register(client, email, name):
    response = client.post("/showSummary", data=email)
    data = response.data.decode()
    name_db = name['name'][0]
    assert f'<h2>Welcome, {name_db} </h2>' in data


def test_show_summary_point_register(client, email, point):
    response = client.post("/showSummary", data=email)
    data = response.data.decode()
    point_db = point['point'][0]
    assert f'<p>Points available: {point_db}</p>' in data

