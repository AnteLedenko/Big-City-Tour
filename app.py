# So in this file im creating all necessary imports creating flask apllication and loading configuration file,
# initialazing database, login manager and registerng blueprints.

from flask import Flask
from flask_login import LoginManager
from models import db, User
from routes import pages, authentication, reviews

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = "authentication.login"

app.register_blueprint(pages)
app.register_blueprint(authentication)
app.register_blueprint(reviews)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == "__main__":
    app.run(debug=True, port=8000)
