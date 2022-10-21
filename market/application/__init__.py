from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///store.db"
database = SQLAlchemy(app)

