from flask import render_template, redirect, url_for
from collectorSite1 import app, db
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
import requests

# signup page and inputing data from user into database, redirect user to home page after


@app.route('/signup', methods=['GET', 'POST'])
def index():
    if requests.method == 'POST':
        email = requests.form.get('email')
        password = requests.form.get('password')
        username = requests.form.get('username')

        new_user = User(email=email, password=generate_password_hash(
            password, method='sha256'), username=username)
        user = User.query.filter_by(email=email).first()
        if user:
            print("User already exists")  # TODO change to flash
        else:
            db.session.add(new_user)
            db.session.commit()
            print("New user created")  # TODO change to flash
            # TODO inside of ulr_for insert the home page route
            return redirect(url_for())
    return render_template('index.html')  # TODO insert the template for signup


@app.route('/login', methods=['GET', 'POST'])
def index():
    if requests.method == 'POST':
        email = requests.form.get('email')
        password = requests.form.get('username')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                print("Logged in successfully")  # TODO change to flash
            else:
                print("Incorrect password")  # TODO change to flash
        else:
            print("User does not exist")  # TODO change to flash

    return render_template('index.html')  # TODO insert the template for login
