from init import db, ma 

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64), nullable = False)
    price = db.Column(db.Integer, nullable = False)



    #relationships
    appointment = db.relationship('Appointment', back_populates = 'services', cascade = 'all, delete')
    barber = db.relationship('Barber', back_populates = 'services')



