from init import db, ma 
from datetime import time

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Time)
    