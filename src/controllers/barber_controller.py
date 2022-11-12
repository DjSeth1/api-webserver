from flask import Blueprint
from init import db
from models.barber import Barber
from schemas.barber_schema import BarberSchema
from flask_jwt_extended import jwt_required

barber_bp = Blueprint('barber', __name__, url_prefix='/barber')

@barber_bp.route('/all_barbers/', methods = ['GET'])
def get_all_barbers():
    '''Checks the database for all barbers and returns all of Barbers in JSON.'''
    stmt = db.select(Barber)
    barbers = db.session.scalars(stmt)
    return BarberSchema(many = True, exclude = ['password']).dump(barbers)

@barber_bp.route('/<int:id>/', methods = ['GET'])
def get_one_barbers(id):
    '''Checks the database for barber and filters it by id. Returns barber JSON'''
    stmt = db.select(Barber).filter_by(id = id)
    barber = db.session.scalar(stmt)
    if barber:
        return BarberSchema(exclude=['password']).dump(barber)
    else:
        return {'error': f'Barber with id {id} does not exist'}, 404

