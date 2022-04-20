from Python_Testing.server import show_summary


def test_show_summary_valide_email(email):
    assert len(email["email"]) == 1


# import flask
# from flask import current_app
# def test_hfdhjfdjdf(app):
#     with app.test_request_context("/"):
#         with current_app.test_request_context():
#             print(flask.request.method)
#             assert flask.request.path == '/'