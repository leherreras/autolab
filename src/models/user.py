import flask_login

from app import db


class User(db.Model, flask_login.UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    api_key = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, api_key, name):
        self.api_key = api_key
        self.name = name

    def __repr__(self):
        return f'User({self.name})'

    def __str__(self):
        return self.name
