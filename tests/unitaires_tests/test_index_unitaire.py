def test_index_check_status_ok(client):
    response = client.get('/')
    assert response.status_code == 200


def test_index_check_render_template(client, captured_templates):
    response = client.get('/')
    template, context = captured_templates[0]
    assert template.name == "index.html"


def test_index_view_text_title(client):
    response = client.get('/')
    expect_out = b"<h1>Welcome to the GUDLFT Registration Portal!</h1>"
    assert expect_out in response.data




