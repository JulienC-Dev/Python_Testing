
def test_index_route_login_page_to_welcome_page(client, email):
    response = client.get("/")
    assert response.status_code == 200
    response = client.post("/showSummary", data=email)
    assert response.status_code == 200

