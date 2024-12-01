# Creating all necessary imports creating a blueprint and then creating a function that quaries
# database and fetches data from tours and reviews of associated city.
# Each city route renders tamplate for the city and displayes the data for city tours and reviews.
# Home route just renders index.html (home page).

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import User, Tour, Review, db

pages = Blueprint('pages', __name__)

def fetch_city_data(city_name):
    tours = Tour.query.filter_by(city=city_name).all()
    reviews = (
        Review.query
        .join(Tour, Review.tour_id == Tour.tour_id)
        .join(User, Review.user_id == User.user_id)
        .filter(Tour.city == city_name)
        .all()
    )
    return tours, reviews


@pages.route('/')
def home():
    return render_template('index.html')

@pages.route('/london')
def london():
    tours, reviews = fetch_city_data("London")
    return render_template('london.html', tours=tours, reviews=reviews)

@pages.route('/glasgow')
def glasgow():
    tours, reviews = fetch_city_data("Glasgow")
    return render_template('glasgow.html', tours=tours, reviews=reviews)

@pages.route('/dublin')
def dublin():
    tours, reviews = fetch_city_data("Dublin")
    return render_template('dublin.html', tours=tours, reviews=reviews)

@pages.route('/cardiff')
def cardiff():
    tours, reviews = fetch_city_data("Cardiff")
    return render_template('cardiff.html', tours=tours, reviews=reviews)
