#!create_db.py
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_TRACK_MODIFICATIONS
from app import db
db.create_all()