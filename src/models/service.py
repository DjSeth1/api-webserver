from init import db

#Model for service table
class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64), nullable = False)
    price = db.Column(db.Integer, nullable = False)



    #relationships
     #each service can have many appointments. 
    
    appointments = db.relationship('Appointment', back_populates = 'service', cascade = 'all, delete')



