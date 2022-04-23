from Python_Testing import server
from Python_Testing.server import formated_data


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


def test_book_valid_url_booking_display(mocker, client, email):
    fake_competitions = [{'name': 'FakeCompetitionName', 'date': '2027-03-27 10:00:00', 'numberOfPlaces': '215'}]
    mocker.patch.object(server, 'competitions', fake_competitions)
    response = client.post("/showSummary", data=email)
    data = response.data.decode()
    assert fake_competitions[0]['date'] > formated_data
    assert 'Book Places' in data


def test_show_summary_invalid_url_booking_display(mocker, client, email):
    fake_competitions = [{'name': 'Spring Festival', 'date': '2020-03-27 10:00:00', 'numberOfPlaces': '215'}]
    mocker.patch.object(server, 'competitions', fake_competitions)
    response = client.post("/showSummary", data=email)
    data = response.data.decode()
    assert fake_competitions[0]['date'] < formated_data
    assert 'Book Places' not in data



# def test_show_summary_point_register(client, email):
#     response = client.post("/showSummary", data=email)
#     data = response.data.decode()
#     input_point = {'point': '2'}
#     input_point = input_point['point']
#     assert f'<p>Points available: {input_point}</p>' in data



# import flask
# from flask import current_app, url_for, request
# def test_hfdhjfdjdf(captured_templates,app):
#     with app.test_request_context(data={'name': 'Spring Festival', 'date': '2020-03-27 10:00:00', 'numberOfPlaces': '215'}):
#         with current_app.test_request_context():
#             print(captured_templates)
#             assert flask.request.path == '/'