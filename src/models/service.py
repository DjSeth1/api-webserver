from init import db, ma 

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    types = db.Column(db.String(64), nullable = False)
    price = db.Column(db.Integer, nullable = False)


    