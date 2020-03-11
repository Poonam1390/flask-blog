from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from os import getenv
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
Login_manager = LoginManager(app)
Login_manager.login_view = 'login'

from application import routes