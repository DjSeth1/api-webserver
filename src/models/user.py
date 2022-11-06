from init import db, ma 



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(64), nullable = False)
    l_name = db.Column(db.String(64))
    email = db.Column(db.String(), nullable = False, unique = True)
    password = db.Column(db.String(), nullable = False)
    phone = db.Column(db.String(40))
    is_admin = db.Column(db.Boolean(), default=False)


    #relationships
    appointments = db.relationship('Appointment', back_populates = 'users', cascade = 'all, delete', uselist = False)
   




