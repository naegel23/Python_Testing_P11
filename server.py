import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


def check_available_points(competitionData, clubData, placesData):
    competition = [c for c in competitions if c['name'] == competitionData][0]
    club = [c for c in clubs if c['name'] == clubData][0]
    competition_places = int(competition['numberOfPlaces'])
    places_required = int(placesData)
    points_available = int(club['points'])
    if places_required < points_available:
        competition['numberOfPlaces'] = competition_places - places_required
        club['points'] = points_available - places_required
        check = False
        return check, club, competition
    elif places_required > 12:
        check = True
        return check, competitionData, clubData
    else:
        check = True
        return check, competitionData, clubData


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    return render_template('welcome.html',club=club,competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    check, club, competition = check_available_points(request.form['competition'], request.form['club'],
                                                      request.form['places'])
    if check is False:
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions, clubs=clubs)
    elif check is True and int(request.form['places']) > 12:
        flash("you can't book more than 12 places")
        return book(request.form['competition'], request.form['club'])
    else:
        flash("You don't have enough points available")
        return book(request.form['competition'], request.form['club'])


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))