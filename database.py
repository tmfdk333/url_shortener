from app import db, models
from sys import argv

db.drop_all()
db.create_all()