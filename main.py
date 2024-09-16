from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv
# Optional: add contact me email functionality (Day 60)
# import smtplib
from flask_babel import Babel
from flask_babel import _, gettext

from forms import *
from functions import *
from databases import *

# Load environment variables
load_dotenv()

def get_locale():
    # print(os.environ.get('LANGUAGES'))
    # return request.accept_languages.best_match(['en', 'bg'])
    return 'en'


# Flask app
app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SECRET_KEY'] = 'secret'
app.config['UPLOAD_EXTENSIONS'] = UPLOAD_EXTENSIONS
app.config['UPLOAD_PATH'] = UPLOAD_PATH

ckeditor = CKEditor(app)
Bootstrap5(app)

# DATA
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        # Check if user email is already present in the database.
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        # This line will authenticate the user with Flask-Login
        # login_user(new_user)
        # return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=form)#, current_user=current_user)

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = AddPropertyForm()
    if form.validate_on_submit():
        print(form.pics.data)
        save_pics(form.pics.data)
    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True, port=5005)

#TODO
# Create page to add or remove property Done
# For the city can be free text Done
# Figure out how to handle images On it Done
# Maybe make a chatgpt agent that use all the available info to write a description
#TODO
# Create a database to store the property information 
#TODO
# Add a button to change the language
#TODO
# Mark all of the translatable fields
# Use chat-gpt for translations
#TODO
#Create the admin view, so only the admin can add/remove properties
