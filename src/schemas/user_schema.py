from init import ma 
from marshmallow import fields


class UserSchema(ma.Schema):

    #validation
    appointments = fields.Nested('AppointmentSchema', exclude =['user'])

    class Meta:


        fields = ('id', 'f_name', 'l_name', 'email','phone','is_admin', 'password', 'appointments')
        ordered = True

