import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime

def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

myDate = datetime.now()
formated_data = myDate.strftime("%Y-%m-%d %H:%M:%S")


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
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]

    except:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions, date=formated_data)
    return render_template('booking.html', club=foundClub, competition=foundCompetition)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
    club['points'] = int(club['points']) - placesRequired
    if club['points'] < 0:
        club['points'] = int(club['points']) + placesRequired
        competition['numberOfPlaces'] = competition['numberOfPlaces'] + placesRequired
        flash('booking not complete! insufficient numbers of points')
        return render_template('welcome.html', club=club, competitions=competitions, date=formated_data)
    if placesRequired <= 0:
        club['points'] = int(club['points']) + placesRequired
        competition['numberOfPlaces'] = competition['numberOfPlaces'] + placesRequired
        flash('booking not complete! invalid numbers of points')
        return render_template('welcome.html', club=club, competitions=competitions, date=formated_data)
    if placesRequired > 12:
        club['points'] = int(club['points']) + placesRequired
        competition['numberOfPlaces'] = competition['numberOfPlaces'] + placesRequired
        flash('booking not complete! cannot book more than 12 persons')
        return render_template('welcome.html', club=club, competitions=competitions, date=formated_data)
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions, date=formated_data)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


# if __name__ == '__main__':
#     app.run(debug=True)