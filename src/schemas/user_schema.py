from init import ma 
from marshmallow import fields, validates
from marshmallow.validate import Length, Regexp


class UserSchema(ma.Schema):

    #validation
    appointments = fields.Nested('AppointmentSchema', only = ['id', 'time', 'barber'])

    #validations
    f_name = fields.String(required = True, validate=Length(min=1, error='First name must be at least 1 character in length'))
    l_name = fields.String(required = True, validate=Length(min=1, error='Last name must be at least 1 character in length'))
    password = fields.String(required = True, validate=Length(min=6), error='Password must be at least 6 characters long')
    email = fields.String(required = True, validate= Regexp("""^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$""", error="Please provide a valid email address"))
    phone = fields.String(required = True, validate= Regexp('^[0-9 ()+]+$', error="Please provide a valid phone number"))




    class Meta:
        fields = ('id', 'f_name', 'l_name', 'email','phone','is_admin', 'password', 'appointments')
        ordered = True

