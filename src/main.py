from flask import Flask
from controllers.cli_controller import db_commands
from init import db, ma, bcrypt, jwt
import os


def create_app():
    app = Flask(__name__)
    #configs
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JSON_SORT_KEYS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')



    #error handles 




    #instances of the components
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


    #registering blueprints from controllers
    app.register_blueprint(db_commands)


    return app