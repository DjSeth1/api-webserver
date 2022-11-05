from init import db, ma 
from datetime import time

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Time)
    #foreign keys
    user = db.relationship('User', back_populates = 'barber', cascade = 'all, delete', uselist = False) 
    service = db.relationship('Service', back_populates = 'appointment', cascade = 'all, delete', uselist = False)
    barber =  db.relationship('Barber', back_populates = 'appointment', cascade = 'all, delete', uselist = False)
