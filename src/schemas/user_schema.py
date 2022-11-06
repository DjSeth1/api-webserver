from init import ma 

class UserSchema(ma.Schema):

    class Meta:
        fields = ('id', 'f_name', 'l_name', 'email','phone','is_admin', 'password')
        ordered = True

