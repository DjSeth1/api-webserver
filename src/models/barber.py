from init import db


#model for barber table.
class Barber(db.Model):
    __tablename__ = 'barbers'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(64), nullable = False)
    l_name = db.Column(db.String(64), nullable = False)
    email = db.Column(db.String(), nullable = False)
    password = db.Column(db.String(), nullable = False)
    phone = db.Column(db.String(), nullable = False)
    is_admin = db.Column(db.Boolean(), default=True)
    time_slots = db.Column(db.String())



    #relationships
    #a barber can have many appointments
    appointments = db.relationship('Appointment', back_populates = 'barber', cascade= 'all, delete')






