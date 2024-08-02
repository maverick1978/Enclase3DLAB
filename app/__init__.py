from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('instance.config.Config')
db = SQLAlchemy(app)

from . import routes
