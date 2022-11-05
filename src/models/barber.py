from init import db, ma 
from datetime import time


class Barber(db.Model):
    __tablename__ = 'barbers'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(64), nullable = False)
    l_name = db.Column(db.String(64), nullable = False)
    email = db.Column(db.String(), nullable = False)
    password = db.Column(db.String(), nullable = False)
    phone = db.Column(db.String(), nullable = False)
    is_admin = db.Column(db.Boolean(), default=False)
    time_slots = db.Column(db.String())
    #foreign keys
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable = False)

    #relationships
    appointments = db.relationship('Appointment', back_populates = 'barbers', cascade = 'all, delete')

    services = db.relationship('Service', back_populates = 'barbers', cascade = 'all, delete')






