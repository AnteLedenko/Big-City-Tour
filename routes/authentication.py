# Creating all necessary imports  creaating a blueprint and then creating four routes that
# handle registration, profile, login and logout.
# In registration route im crating function that recives data from registration form then checks if
# username is available if not redirects back to register page if available generates hashed password 
# and then saves users data to database and redirects to home page.
# In profile route just setting up login required decorator to acces the page only if logged in
# and function profile that gets all currently logged in users reviews and returns profile page.
# Login route here we have login functionn that requests username and password  and if they match
# user gets logged in and redirected to home page. 
# Just like profile page only can be accesed if user is logged in and the rout just redirects to login page
# after logout is comfirmed. 

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Review, db
from datetime import datetime

authentication = Blueprint('authentication', __name__)

@authentication.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        date = request.form["date"]
        join_date = datetime.strptime(date, "%Y-%m-%d").date()

        if User.query.filter_by(username=username).first():
            return redirect(url_for("authentication.register"))

        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password, email=email, join_date=join_date)

        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for('pages.home'))
    
    return render_template('register.html')


@authentication.route('/profile', methods=['GET','POST'])
@login_required
def profile(): 
    user_reviews = Review.query.filter_by(user_id=current_user.user_id).all()

    return render_template('profile.html', user=current_user, reviews=user_reviews)


@authentication.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('pages.home'))
        else:
            return redirect(url_for('authentication.login'))

    return render_template('login.html')


@authentication.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    if request.method == 'POST':
        logout_user()
        return redirect(url_for('authentication.login'))
    return render_template('logout.html')
