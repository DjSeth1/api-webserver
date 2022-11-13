from flask import Blueprint, request
from init import db
from models.appointment import Appointment
from schemas.appointment_schema import AppointmentSchema
from models.user import User



from flask_jwt_extended import get_jwt_identity, jwt_required



appointment_bp = Blueprint('appointment', __name__, url_prefix='/appointment')

#CREATE APPOINTMENT

@appointment_bp.route('create/<int:user_id>', methods = ['POST'])
@jwt_required()
def create_appointment(user_id):
    '''Creates appointment for a registered user and checks for jwt token to identify the user. Once identified the user can create the appointment using the appointment schemas and model.'''
    user_id = get_jwt_identity()
    data = AppointmentSchema().load(request.json)
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)

    if user:
        appointment = Appointment(
            time = data.get('time'),
            user = user_id,
            barber = data.get('barber'),
            service = data.get('service')

        )
        db.session.add(appointment)
        db.session.commit()

        return {'success': 'You have successfully created an appointment', 'appointment': AppointmentSchema().dump(appointment)}

    else:
        return {'error': 'This user does not exist'}
    





#READ ALL
@appointment_bp.route('/all_appointments/', methods=['GET'])
def get_all_appointments():
    '''Get method to gather all appointments'''
    stmt = db.select(Appointment)
    appointments = db.session.scalars(stmt)
    return AppointmentSchema(many = True).dump(appointments)


#READ ONE APPOINTMENT
@appointment_bp.route('/<int:id>/', methods = ['GET'])
@jwt_required()
def get_one_appointment(id):
    '''Reads one single appointment by given ID of the appointment. Checks to see if appointment exists, if not returns error.'''
    stmt = db.select(Appointment).filter_by(id=id)
    appointment = db.session.scalar(stmt)
    if appointment:
        return AppointmentSchema().dump(appointment)
    else:
        return {'error': f'No such appointment with this id {id}'}, 404



#READ ONE APPONTMENT (USERS OWN APPOINTMENT)
@appointment_bp.route('/user_appointment/<int:user_id>', methods = ['GET'])
@jwt_required()
def get_user_appointment(user_id):
    '''User can search for their own appointment. First this functioin checks database to confirm the user through JWT, then it checks if there is an appointment under that name. If there is, appointment details are  shown excluding the user details since the user is the one checking their own appointment, otherwise no appointment error is returned.'''
    
    user_id = get_jwt_identity()
    stmt = db.select(Appointment).filter_by(user_id = user_id)
    appointment = db.session.scalar(stmt)
    db.session.scalar(stmt)
    if appointment:
        return AppointmentSchema(exclude = ['user']).dump(appointment)
    else:
        return {'error': f'This user does not have an appointment with id {user_id}'}, 404


#UPDATE existing Appointment BY USER
@appointment_bp.route('/user_appointment/<int:user_id>', methods = ['POST', 'PATCH'])
@jwt_required()
def update_user_appointment(user_id):
    '''User can update their own appointment. First it checks for users verification, then once verified it allows user to update their appointment. If no appointment exists, it will show there is no appointment under that user's id.'''
    user_id = get_jwt_identity()
    stmt = db.select(Appointment).filter_by(user_id = user_id)
    appointment = db.session.scalar(stmt)
    if appointment:
        data = AppointmentSchema().load(request.json)
        appointment.time = data['time'] or appointment.time
        appointment.service = data['service'] or appointment.service
        appointment.user = appointment.user
        appointment.barber = appointment.barber
        
        db.session.commit()
        return {
            'success' : 'You have updated your appointment successfully.', 'appointment details' : AppointmentSchema(exclude= ['user']).dump(appointment)
        }
    else:
        return {'error': f'Appointment of user with id {user_id} does not exist'}, 404

#DELETE EXISTING APPOINTMENT
@appointment_bp.route('/user_appointment/<int:user_id>', methods = ['DELETE'])
@jwt_required()
def delete_user_appointment(user_id):
    '''User can delete their own appointment. First checks for for user;s authorisation via JWT identity. If there is a match, it will proceed onto allowing user to delete appointment. If authorisation fails or there is no appointment under that user it will return an error.'''
    user_id = get_jwt_identity()
    stmt = db.select(Appointment).filter_by(user_id = user_id)
    appointment = db.session.scalar(stmt)
    if appointment:
        db.session.delete(appointment)
        db.session.commit()
        return {'success': f'The appointment for user {user_id} were successfully deleted'}
    else:
        return {'error': f'The appointment for user {user_id} was not found'}, 404










    











