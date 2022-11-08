from init import ma 
from marshmallow import fields

class AppointmentSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude = ['', 'password'])
    barber = fields.Nested('BarberSchema', only = ['f_name', 'l_name', 'phone'])

    class Meta:
        fields = ('id', 'barber', 'user', 'service_id','time')
        ordered = True
