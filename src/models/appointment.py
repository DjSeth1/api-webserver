from init import db


#Model for Appointment Table.

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String())
    
    #foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    barber_id = db.Column(db.Integer, db.ForeignKey('barbers.id'), nullable = False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable = False)
    
    #relationships
    #appointment can have one user
    user = db.relationship('User', back_populates = 'appointment', uselist = False, cascade = 'all, delete')
    #appointment can have one barber
    barber = db.relationship('Barber', back_populates = 'appointments', cascade = 'all, delete')
    #appointment can have one service.
    service = db.relationship('Service', back_populates = 'appointments', cascade = 'all, delete')


