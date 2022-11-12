from flask import Blueprint
from init import db
from models.service import Service
from schemas.service_schema import ServiceSchema
from flask_jwt_extended import jwt_required


service_bp = Blueprint('service', __name__, url_prefix='/service')

#view services

@service_bp.route('/all_services/', methods = ['GET'])
@jwt_required()
def get_all_services():
    '''Route returns all services available by querying the database for all services under services table.'''
    stmt = db.select(Service)
    services = db.session.scalars(stmt)
    return ServiceSchema(many = True).dump(services)


#view service by id

@service_bp.route('/<int:id>/', methods = ['GET'])
@jwt_required()
def get_one_service(id):
    '''Checks database for all services with a specific id, then returns the service by id. If no such id is found, it returns an error'''
    stmt = db.select(Service).filter_by(id=id)
    service = db.session.scalar(stmt)
    if service:
        return ServiceSchema().dump(service)
    else:
        return {'error':f'Service with id {id} does not exist'}, 404


    


