from Python_Testing import server


def test_route_summary_valid_user_booking_page_url(mocker, app):
    fake_club = [{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}]
    input_places_desire = "3"
    fake_competition = [{
        "name": "Spring Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25"
    }]
    valid_email = {"email": ["admin@irontemple.com"]}
    with app.test_client() as client:
        mocker.patch.object(server, 'clubs', fake_club)
        response = client.post('/showSummary', data=valid_email, follow_redirects=True)
        mocker_competition = mocker.patch.object(server, 'competitions', fake_competition)
        club_name = fake_club[0]['name']
        name_competion = fake_competition[0]['name']
        res = client.post('/purchasePlaces', data=dict(club=club_name, competition=name_competion,
                                                      places=input_places_desire),)
        assert res.status_code == 200






