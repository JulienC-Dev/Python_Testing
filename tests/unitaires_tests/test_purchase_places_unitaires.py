from Python_Testing import server


def test_purchase_places_valid_balance_point_club_and_point_competition(mocker, client):
    input_places_desire = "2"
    expected_output_points_club = 0
    expected_competition_points = 15
    fake_club = [{
        "name": "le club fake 1",
        "email": "jj@simplylift.co",
        "points": "6"
    }]
    fake_competition = [{
        "name": "Test Fake compétition 1",
        "date": "2027-03-27 10:00:00",
        "numberOfPlaces": "16"
    }]
    club_name = fake_club[0]['name']
    name_competion = fake_competition[0]['name']
    mocker_club = mocker.patch.object(server, 'clubs', fake_club)
    mocker_competition = mocker.patch.object(server, 'competitions', fake_competition)
    response = client.post('/purchasePlaces',
                           data=dict(club=club_name, competition=name_competion, places=input_places_desire),
                           )
    data = response.data.decode()
    point_club = int(fake_club[0]['points'])
    assert int(fake_club[0]['points']) == expected_output_points_club
    assert f'<p>Points available: {point_club}</p>' in data
    assert '<li>Great-booking complete!</li>' in data

    assert int(fake_competition[0]['numberOfPlaces']) == expected_competition_points
    points_competition = int(fake_competition[0]['numberOfPlaces'])
    assert f'Number of Places: {points_competition}' in data


def test_purchase_place_more_than_balance(mocker, client):
    input_places_desire = "10"
    fake_club = [{
        "name": "le club fake 1",
        "email": "jj@simplylift.co",
        "points": "5"
    }]
    fake_competition = [{
        "name": "Test Fake compétition 1",
        "date": "2027-03-27 10:00:00",
        "numberOfPlaces": "16"
    }]
    club_name = fake_club[0]['name']
    name_competion = fake_competition[0]['name']
    mocker_club = mocker.patch.object(server, 'clubs', fake_club)
    mocker_competition = mocker.patch.object(server, 'competitions', fake_competition)
    response = client.post('/purchasePlaces',
                           data=dict(club=club_name, competition=name_competion, places=input_places_desire),
                           )
    data = response.data.decode()
    assert int(input_places_desire) > int(fake_club[0]['points'])
    assert '<li>booking not complete! insufficient numbers of points</li>' in data


def test_purchase_place_negative_input(mocker, client):
    input_places_desire = "-10"
    fake_club = [{
        "name": "le club fake 1",
        "email": "jj@simplylift.co",
        "points": "5"
    }]
    fake_competition = [{
        "name": "Test Fake compétition 1",
        "date": "2027-03-27 10:00:00",
        "numberOfPlaces": "16"
    }]
    club_name = fake_club[0]['name']
    name_competion = fake_competition[0]['name']
    mocker_club = mocker.patch.object(server, 'clubs', fake_club)
    mocker_competition = mocker.patch.object(server, 'competitions', fake_competition)
    response = client.post('/purchasePlaces',
                           data=dict(club=club_name, competition=name_competion, places=input_places_desire),
                           )
    data = response.data.decode()
    assert int(input_places_desire) < 0
    assert '<li>booking not complete! invalid numbers of points</li>' in data


def test_purchase_place_zero_input(mocker, client):
    input_places_desire = "0"
    fake_club = [{
        "name": "le club fake 1",
        "email": "jj@simplylift.co",
        "points": "24"
    }]
    fake_competition = [{
        "name": "Test Fake compétition 1",
        "date": "2027-03-27 10:00:00",
        "numberOfPlaces": "16"
    }]
    club_name = fake_club[0]['name']
    name_competion = fake_competition[0]['name']
    mocker_club = mocker.patch.object(server, 'clubs', fake_club)
    mocker_competition = mocker.patch.object(server, 'competitions', fake_competition)
    response = client.post('/purchasePlaces',
                           data=dict(club=club_name, competition=name_competion, places=input_places_desire),
                           )
    data = response.data.decode()
    assert int(input_places_desire) == 0
    assert '<li>booking not complete! invalid numbers of points</li>' in data


def test_purchase_place_more_than_12(mocker, client):
    input_places_desire = "13"
    fake_club = [{
        "name": "le club fake 1",
        "email": "jj@simplylift.co",
        "points": "24"
    }]
    fake_competition = [{
        "name": "Test Fake compétition 1",
        "date": "2027-03-27 10:00:00",
        "numberOfPlaces": "16"
    }]
    club_name = fake_club[0]['name']
    name_competion = fake_competition[0]['name']
    mocker_club = mocker.patch.object(server, 'clubs', fake_club)
    mocker_competition = mocker.patch.object(server, 'competitions', fake_competition)
    response = client.post('/purchasePlaces',
                           data=dict(club=club_name, competition=name_competion, places=input_places_desire),
                           )
    data = response.data.decode()
    assert int(input_places_desire) > 12
    assert 'booking not complete! cannot book more than 12 persons' in data


def test_purchase_place_more_than_places_competition_available(mocker, client):
    input_places_desire = "12"
    fake_club = [{
        "name": "le club fake 1",
        "email": "jj@simplylift.co",
        "points": "24"
    }]
    fake_competition = [{
        "name": "Test Fake compétition 1",
        "date": "2027-03-27 10:00:00",
        "numberOfPlaces": "3"
    }]
    expected_output_places_competition = 3
    club_name = fake_club[0]['name']
    name_competion = fake_competition[0]['name']
    mocker_club = mocker.patch.object(server, 'clubs', fake_club)
    mocker_competition = mocker.patch.object(server, 'competitions', fake_competition)
    response = client.post('/purchasePlaces',
                           data=dict(club=club_name, competition=name_competion, places=input_places_desire),
                           )
    data = response.data.decode()
    assert fake_competition[0]['numberOfPlaces'] == expected_output_places_competition
    assert int(input_places_desire) > int(fake_competition[0]['numberOfPlaces'])
    assert f'Number of Places: {expected_output_places_competition}' in data
    assert '<li>booking not complete! not enough places available for this competition</li>' in data
