import os
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

from werkzeug.security import generate_password_hash, check_password_hash

from . import main
from .. import db
from ..models import Quote, Submission, User
from .forms import *

from dotenv import load_dotenv

load_dotenv()

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/database")
def database():
    return render_template("database.html")

@main.route("/random")
def random():
    return render_template("random.html")

@main.route("/submit", methods=['GET','POST'])
def submit():
    form = SubmitForm()
    submitted = None
    if form.validate_on_submit():
        addSubmission(form.author.data, form.quote.data, form.tags.data)
        submitted = "Quote Submitted!"
    return render_template("submit.html", form=form, submitted=submitted)  

@main.route("/admin-review-submissions", methods=['GET','POST'])
@login_required
def review_submission():
    return render_template("review-submissions.html", submissions=getSubmissions())  

@main.route("/admin-sign-up", methods=['GET','POST'])
def admin_sign_up():
    form = SignUpForm()
    signed_up = None
    if form.validate_on_submit():
        signed_up = validateSignUp(form.admin_key.data, form.username.data, form.password.data, form.confirm_password.data)
    return render_template("admin-sign-up.html", form=form, signed_up=signed_up)     

@main.route("/admin-login", methods=['GET','POST'])
def admin_login():
    form = LoginForm()
    logged_in = None
    if form.validate_on_submit():
        logged_in = validateLogin(form.username.data, form.password.data)
    return render_template("admin-login.html", form=form, logged_in=logged_in)     

@main.route("/admin-logout")
@login_required
def admin_logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("main.index"))

def addUser(username, password):
    hashed = generate_password_hash(password)
    print(hashed)
    user = User(username=username, password=hashed)
    db.session.add(user)
    db.session.commit()

def getUser(username):
    return User.query.filter_by(username=username).first()

def validateSignUp(admin_key, username, password, confirm_password):
    if admin_key != os.getenv("ADMIN_KEY"):
        return "Incorrect admin key!"
    
    check_username = getUser(username)
    if password == confirm_password and check_username is None:
        addUser(username, password)
        signed_up = "Admin account sign-up successful!"
    elif check_username is not None:
        signed_up = "Username already exists!"
    else:
        signed_up = "Passwords do not match!"

    return signed_up

def validateLogin(username, password):
    user = getUser(username)
    if user is not None and check_password_hash(user.password, password):
        login_user(user)
        logged_in = "Login successful!"
    else:
        logged_in = "Incorrect username or password."

    return logged_in

def addSubmission(author, quote, tags):
    submission = Submission(author=author, quote=quote, tags=tags)
    db.session.add(submission)
    db.session.commit()

def getSubmissions():
    return Submission.query.all()

def addQuote(author, quote, tags):
    quote_ = Quote(author=author, quote=quote, tags=tags)
    db.session.add(quote_)
    db.session.commit()