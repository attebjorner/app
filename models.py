from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint, func
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('user', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.Text)
    bitrhday = db.Column('bitrhday', db.Text)


class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    text = db.Column('text', db.Text)


class Answers(db.Model):
    __tablename__ = 'answers'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    q_fool = db.Column('q_fool', db.Text)
    q_walla = db.Column('q_walla', db.Text)
    q_def = db.Column('q_def', db.Text)
