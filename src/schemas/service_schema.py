from init import ma 

class ServiceSchema(ma.Schema):
    

    class Meta:
        fields = ('id', 'type', 'price')