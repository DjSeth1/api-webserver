from flask import Blueprint, request
from init import db, bcrypt
from datetime import timedelta
from models.appointment import Appointment
from schemas.appointment_schema import AppointmentSchema

from flask_jwt_extended import get_jwt_identity



appointment_bp = Blueprint('appointment', __name__, url_prefix='/appointment')


@appointment_bp.route('/all_appointments/', methods=['GET'])
def get_all_appointments():
    stmt = db.select(Appointment)
    appointments = db.session.scalars(stmt)
    return AppointmentSchema(many = True).dump(appointments)






