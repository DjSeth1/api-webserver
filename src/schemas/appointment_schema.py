from init import ma 
from marshmallow import fields, validates
from marshmallow.validate import OneOf


VALID_TIMES = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00']
VALID_SERVICE_ID = [1, 2]

class AppointmentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['id','f_name','l_name'])
    barber = fields.Nested('BarberSchema', only=['f_name','l_name'])
    service = fields.Nested('ServiceSchema', exclude=['id'])
 

    #validations
    time = fields.String(required = True, validate=OneOf(VALID_TIMES, error=f'The time selected must be one of {VALID_TIMES}'))
    service_id = fields.Integer(required = True, validate = OneOf(VALID_SERVICE_ID, error=f'Please enter valid service {VALID_SERVICE_ID}'))

    class Meta:
        fields = ('id','time', 'barber', 'service', 'user', 'user_id', 'barber_id', 'service_id',)
        ordered = True
