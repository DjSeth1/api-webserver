from flask import Flask
from controllers.cli_controller import db_commands
from controllers.auth_controller import auth_bp
from controllers.user_controller import user_bp
from controllers.appointment_controller import appointment_bp
from controllers.service_controller import service_bp
from controllers.barber_controller import barber_bp
from marshmallow.exceptions import ValidationError
from init import db, ma, bcrypt, jwt
import os


def create_app():
    app = Flask(__name__)
    #configs
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JSON_SORT_KEYS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')



    #error handles 
    @app.errorhandler(401)
    def unauthorized():
        return {'error': 'You are not authorized to perform this action'}, 401

    @app.errorhandler(404)
    def not_found(err):
        return {'error': str(err)}, 404
    
    @app.errorhandler(400)
    def bad_request(err):
        return {'error': str(err)}, 400
    
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.messages}, 400
    
    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The field {err} is required.'}, 400


    #instances of the components
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


    #registering blueprints from controllers
    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(appointment_bp)
    app.register_blueprint(service_bp)
    app.register_blueprint(barber_bp)


    return app