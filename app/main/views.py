from flask import render_template, url_for

from . import main
from .. import db
from .forms import *

@main.route("/")
def index():
    return render_template("index.html")
