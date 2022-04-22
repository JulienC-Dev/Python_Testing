

def test_purchase_places_valid_balance(client, name, name_competion, point_club):
    input_places_desire = "2"
    assert int(point_club['point'][0]) - int(input_places_desire) == 2
    name = name['name']
    name_competion = name_competion['name']
    response = client.post('/purchasePlaces', data=dict(club=name, competition=name_competion, places=input_places_desire),
                           follow_redirects=True )
    data = response.data.decode()
    point_club = int(point_club['point'][0]) - int(input_places_desire)
    assert f'<p>Points available: {point_club}</p>' in data
    assert '<li>Great-booking complete!</li>' in data


def test_purchase_place_more_than_balance(client, name, name_competion, point_club):
    input_places_desire = "10"
    assert int(input_places_desire) > int(point_club['point'][0])
    name = name['name']
    name_competion = name_competion['name']
    response = client.post('/purchasePlaces', data=dict(club=name, competition=name_competion, places=input_places_desire),
                           follow_redirects=True )
    data = response.data.decode()
    assert '<li>booking not complete! insufficient numbers of points</li>' in data


def test_purchase_place_negative_input(client, name, name_competion):
    input_places_desire = "-10"
    assert int(input_places_desire) < 0
    name = name['name']
    name_competion = name_competion['name']
    response = client.post('/purchasePlaces',
                           data=dict(club=name, competition=name_competion, places=input_places_desire),
                           follow_redirects=True)
    data = response.data.decode()
    assert '<li>booking not complete! insufficient numbers of points</li>' in data

