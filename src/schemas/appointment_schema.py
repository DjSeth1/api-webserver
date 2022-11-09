from init import ma 
from marshmallow import fields


class AppointmentSchema(ma.Schema):
    user = fields.Nested('UserSchema')
    barber = fields.Nested('BarberSchema')
    service = fields.Nested('ServiceSchema')

    class Meta:
        fields = ('id','time', 'barber', 'service', 'user')
        ordered = True
