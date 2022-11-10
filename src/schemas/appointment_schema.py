from init import ma 
from marshmallow import fields
from schemas.barber_schema import BarberSchema
from schemas.service_schema import ServiceSchema


class AppointmentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['id','f_name','l_name','phone','email'])
    barber = fields.Nested('BarberSchema', only=['f_name','l_name'])
    service = fields.Nested('ServiceSchema', exclude=['id'])

    class Meta:
        fields = ('id','time', 'barber', 'service', 'user')
        ordered = True
