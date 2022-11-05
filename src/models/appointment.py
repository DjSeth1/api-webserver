from init import db, ma 
from datetime import time

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String())
    #foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    barber_id = db.Column(db.Integer, db.ForeignKey('barbers.id'), nullable = False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable = False)

    #relationships
    users = db.relationship('User', back_populates = 'appointments', uselist = False)
    barbers = db.relationship('Barber', back_populates = 'appointments')
    services = db.relationship('Service', back_populates = 'appointments')