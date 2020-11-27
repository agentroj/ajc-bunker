from flask import Flask
from pytweet_auth.database import init_db
from pytweet_auth.config import Config
import os
import pytweet_auth.models
from flask_login import LoginManager

def create_app():
    _app = Flask(__name__)
    _app.config.from_object(Config)
    
    _app.secret_key = os.urandom(24)

    init_db(_app)

    return _app

app = create_app()
