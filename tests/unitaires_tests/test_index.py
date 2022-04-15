from Python_Testing import server

import pytest


def test_index_check_status_ok(client):
    response = client.get('/')
    assert response.status_code == 200


def test_index_view_text_title(client):
    response = client.get('/')
    expect_out = b"<h1>Welcome to the GUDLFT Registration Portal!</h1>"
    assert expect_out in response.data


# controler l'apparition du formulaire sur la page index / fichier test_index-non
# contrôler l'url de la page index '/'  / fichier test_index-non



# contrôler que le formulaire n'est pas vide lors d'une méthode Post/ fichier test_showSummary
# contrôler la redirection de la page index vers la page /showSummary'/ fichier test_showSummary/test intégration
# contrôler que l'email renseigné dans le formulaire soit bien une donnée email



# def test_index_form_not_empty(client):
#     data = None
#     response = client.post('/', data=data)
#     assert response.status_code == 200


# def test_index_redirect_invalide(client):
#     response = client.post('/')
#     assert response.request.path == "/"