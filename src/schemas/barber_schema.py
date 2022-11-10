from init import ma 
from marshmallow import fields



class BarberSchema(ma.Schema):

    appointments = fields.List(fields.Nested('AppointmentSchema', only = ['id', 'time', 'user', 'service']))


    class Meta:
        fields = ('id', 'f_name', 'l_name', 'phone', 'email', 'password', 'is_admin', 'time_slots', 'service_id')
        ordered = True