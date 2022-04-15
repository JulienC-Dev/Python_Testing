

# def test_show_summary_empty(client):
#     """
#     #     GIVEN - What are the initial conditions for the test ?
#     #     Client avec data email vide
#     #     WHEN - What is occurring that needs to be tested ?
#     #     THEN - What is the expected response ?
#     #     avoir un status 200 sur le endpoint "/"
#     #     """
#     response = client.post('/showSummary', data={'email': ''})
#     assert response.status_code == 200



# def test_show_valid_email(client):
#     """
#     GIVEN - What are the initial conditions for the test ?
#     Client avec un data email vide
#     WHEN - What is occurring that needs to be tested ?
#     THEN - What is the expected response ?
#     avoir un status 200 sur le endpoint "/"
#     """
#     data = {
#         "email": ""
#     }
#     response = client.post('/',data=data)
#     assert response.status_code == 200
#
# #