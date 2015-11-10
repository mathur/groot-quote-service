import datetime

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Quote(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime)
    text = db.Column(db.String(350), unique=True)
    user_id = db.Column(db.Integer)

    def __init__(self, text, user_id):
        self.text = text
        self.user_id = user_id
        self.time_created = datetime.datetime.now()

    def __repr__(self):
        return '<Quote %r>' % self.id