from flask import Flask
from init import db, ma, bcrypt, jwt


def create_app():
    app = Flask(__name__)

    #configs

    


    #error handles 




    #instances of the components
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


    #registering blueprints from controllers



    return app