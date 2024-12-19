import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
