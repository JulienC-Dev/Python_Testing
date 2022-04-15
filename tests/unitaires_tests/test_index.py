

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