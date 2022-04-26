import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()

my_date = datetime.now()
formated_data = my_date.strftime("%Y-%m-%d %H:%M:%S")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    email = request.form['email']
    list_clubs_email = [club for club in clubs if club['email'] == email]
    if len(list_clubs_email) == 0:
        return render_template('index.html', error="Email non trouvé")
    return render_template('welcome.html', club=list_clubs_email[0], competitions=competitions, date=formated_data)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    try:
        found_club = [c for c in clubs if c['name'] == club][0]
        found_competition = [c for c in competitions if c['name'] == competition][0]
    except:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions, date=formated_data)
    return render_template('booking.html', club=found_club, competition=found_competition)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
    club['points'] = int(club['points']) - places_required
    if competition['numberOfPlaces'] < 0:
        club['points'] = int(club['points']) + places_required
        competition['numberOfPlaces'] = competition['numberOfPlaces'] + places_required
        flash('booking not complete! not enough places available for this competition')
        return render_template('welcome.html', club=club, competitions=competitions, date=formated_data)
    if places_required <= 0:
        club['points'] = int(club['points']) + places_required
        competition['numberOfPlaces'] = competition['numberOfPlaces'] + places_required
        flash('booking not complete! invalid numbers of points')
        return render_template('welcome.html', club=club, competitions=competitions, date=formated_data)
    if places_required > 12:
        club['points'] = int(club['points']) + places_required
        competition['numberOfPlaces'] = competition['numberOfPlaces'] + places_required
        flash('booking not complete! cannot book more than 12 persons')
        return render_template('welcome.html', club=club, competitions=competitions, date=formated_data)

    club['points'] = int(club['points']) + places_required
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) + places_required
    places_required = int(request.form['places']) * 3
    club['points'] = int(club['points']) - places_required
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
    if club['points'] < 0:
        club['points'] = int(club['points']) + places_required
        competition['numberOfPlaces'] = competition['numberOfPlaces'] + places_required
        flash('booking not complete! insufficient numbers of points')
        return render_template('welcome.html', club=club, competitions=competitions, date=formated_data)
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) + places_required -1
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions, date=formated_data)


@app.route('/boardClubs')
def board_clubs():
    return render_template('boardclub.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
