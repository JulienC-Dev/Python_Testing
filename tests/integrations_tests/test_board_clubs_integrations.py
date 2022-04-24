from Python_Testing import server


def test_board_club_render_valid_points_after_purchase_places(mocker, client):
    input_places_desire = "3"
    fake_club = [{
        "name": "le club fake 1",
        "email": "jj@simplylift.co",
        "points": "24"
    }]
    fake_competition = [{
        "name": "Spring Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25"
    }]
    expected_points_output = "21"
    club_name = fake_club[0]['name']
    name_competion = fake_competition[0]['name']
    mocker_club = mocker.patch.object(server, 'clubs', fake_club)
    mocker_competition = mocker.patch.object(server, 'competitions', fake_competition)
    response = client.post('/purchasePlaces',
                           data=dict(club=club_name, competition=name_competion, places=input_places_desire),
                           )
    res = client.get("/boardClubs")
    data = res.data.decode()
    assert int(fake_club[0]['points']) == int(expected_points_output)
    fake_points_club = int(fake_club[0]['points'])
    assert f'<td>{fake_points_club}</td>' in data



