from flask import Flask
from config import Config

# import for Flask DB and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app= Flask(__name__)

app.config.from_object(Config)  # pulling in our config calss

db= SQLAlchemy(app)
migrate = Migrate(app,db)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
from july_blog import routes  # don't need lines 8-10 , we have them in routes
from july_blog import models

