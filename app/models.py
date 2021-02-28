from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# from sqlalchemy import Table, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# user_exercise_table = Table('user_exercise_table', Base.metadata,
#     Column('user_id', Integer, ForeignKey('user.id')),
#     Column('exercise_id', Integer, ForeignKey('exercise.id'))
# )

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # exercises = relationship(
    #                 "Exercise",
    #                 secondary=user_exercise_table,
    #                 backref="users")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)  

class Exercise(db.Model):
    __tablename__ = 'exercise'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    subtitle =  db.Column(db.String(64))
    description = db.Column(db.String(120))
    # users = relationship(
    #     "User",
    #     secondary=user_exercise_table,
    #     back_populates="exercises")

    def __repr__(self):
        return '<Exercise {}>'.format(self.name)  

@login.user_loader
def load_user(id):
    return User.query.get(int(id))