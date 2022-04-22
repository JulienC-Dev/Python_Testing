
def test_show_summary_valide_email(email):
    assert len(email["email"]) == 1


def test_show_summary_not_allowed(client):
    response = client.get("/showSummary")
    assert response.status_code == 405


def test_show_summary_title_register(client, email, name):
    response = client.post("/showSummary", data=email)
    data = response.data.decode()
    name_db = name['name'][0]
    assert f'<h2>Welcome, {name_db} </h2>' in data


# def test_show_summary_point_register(client, email):
#     response = client.post("/showSummary", data=email)
#     data = response.data.decode()
#     input_point = {'point': '2'}
#     input_point = input_point['point']
#     assert f'<p>Points available: {input_point}</p>' in data





# import flask
# from flask import current_app, url_for, request
# def test_hfdhjfdjdf(app):
#     with app.test_request_context("/"):
#         with current_app.test_request_context():
#             assert flask.request.path == '/'