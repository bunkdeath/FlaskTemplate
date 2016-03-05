#!/usr/bin/env python

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


# Define the WSGI application object
app = Flask(__name__)
app.config.from_object('settings')

connection = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)

# START Import a module / component using its blueprint handler variable
# END Import a module

# START Register blueprints
# END Register blueprints
