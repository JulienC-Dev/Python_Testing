from Python_Testing.server import book

from flask import current_app, url_for, request


def test_book_valid_data_url(client, app, name, name_competion):
    name_competion = name_competion["name"][0]
    name = name["name"][0]
    with client:
        with app.app_context():
            assert client.get(url_for('book', club=name, competition=name_competion)).status_code == 200


def test_book_invalid_data_url(client, app):
    name_competion = "invalid Name competition"
    name = "invalid Name club"
    with client:
        with app.app_context():
            res = client.get(url_for('book', club=name, competition=name_competion), follow_redirects=True)
            data = res.data.decode()
            assert '<li>Something went wrong-please try again</li>' in data
            assert res.status_code == 200