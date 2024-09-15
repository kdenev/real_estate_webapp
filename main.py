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
from forms import AddPropertyForm, LoginForm, TestForm

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
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.jpeg']
app.config['UPLOAD_PATH'] = 'uploads'


ckeditor = CKEditor(app)
Bootstrap5(app)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    form = TestForm()
    if form.validate_on_submit():
        print(form.pics.data)
        for p in form.pics.data:
            print(p.filename)
            filename = secure_filename(p.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                    abort(400)
                p.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True, port=5005)

#TODO
# Create page to add or remove property Done
# For the city can be free text Done
# Figure out how to handle images On it
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
