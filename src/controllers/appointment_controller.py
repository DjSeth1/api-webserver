from flask import Blueprint, request
from init import db, bcrypt
from datetime import timedelta
from models.appointment import Appointment
from schemas.appointment_schema import AppointmentSchema
from models.user import User



from flask_jwt_extended import get_jwt_identity, jwt_required



appointment_bp = Blueprint('appointment', __name__, url_prefix='/appointment')

#CREATE APPOINTMENT

@appointment_bp.route('/', methods = ['POST'])
#@jwt_required()
def create_appointment():
    data = AppointmentSchema().load(request.json)
    stmt = db.select(User).filter_by(id = id)
    user = db.session.scalar(stmt)

    if user:
        appointment = Appointment(
            time = data['time'],
            user = get_jwt_identity(),
            barber = data['barber'],
            service = data['service']
,
        )
        db.session.add(appointment)
        db.session.commit()

        return {'success': 'You have successfully created an appointment', 'appointment': AppointmentSchema().dump(appointment)}

    else:
        {'error': 'This user does not exist'}
    





#READ ALL
@appointment_bp.route('/all_appointments/', methods=['GET'])
def get_all_appointments():
    stmt = db.select(Appointment)
    appointments = db.session.scalars(stmt)
    return AppointmentSchema(many = True).dump(appointments)


#READ ONE APPOINTMENT
@appointment_bp.route('/<int:id>/', methods = ['GET'])
def get_one_appointment(id):
    stmt = db.select(Appointment).filter_by(id=id)
    appointment = db.session.scalar(stmt)
    if appointment:
        return AppointmentSchema().dump(appointment)
    else:
        return {'error': f'No such appointment with this id {id}'}, 404



#READ ONE APPONTMENT (USERS OWN APPOINTMENT)
@appointment_bp.route('/user_appointment/<int:user_id>', methods = ['GET'])
#@jwt_required()
def get_user_appointment(user_id):
    stmt = db.select(Appointment).filter_by(user_id = user_id)
    appointment = db.session.scalar(stmt)
    db.session.scalar(stmt)
    if appointment:
        return AppointmentSchema().dump(appointment)
    else:
        return {'error': f'This user does not have an appointment with id {user_id}'}, 404


#UPDATE existing Appointment
@appointment_bp.route('/user_appointment/<int:user_id>', methods = ['POST', 'PATCH'])
#jwt required
def update_user_appointment(user_id):
    stmt = db.select(Appointment).filter_by(user_id = user_id)
    appointment = db.session.scalar(stmt)
    if appointment:
        data = AppointmentSchema().load(request.json)
        appointment.time = data['time'] or appointment.time
        appointment.service = appointment.service
        appointment.user = appointment.user
        appointment.barber = appointment.barber
        
        db.session.commit()
        return {
            'success' : 'You have updated your appointment successfully.', 'appointment details' : AppointmentSchema().dump(appointment)
        }
    else:
        return {'error': f'Appointment of user with id {user_id} does not exist'}, 404

#DELETE EXISTING APPOINTMENT
@appointment_bp.route('/user_appointment/<int:user_id>', methods = ['DELETE'])
def delete_user_appointment(user_id):
    stmt = db.select(Appointment).filter_by(user_id = user_id)
    appointment = db.session.scalar(stmt)
    if appointment:
        db.session.delete(appointment)
        db.session.commit()
        return {'success': f'The appointment for user {user_id} were successfully deleted'}
    else:
        return {'error': f'The appointment for user {user_id} was not found'}, 404










    











