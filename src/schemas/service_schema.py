from init import ma 
from marshmallow import fields, validates
from marshmallow.validate import OneOf

VALID_TYPES = ['Hair', 'Hair and Beard']
VALID_PRICES = [30, 45]

class ServiceSchema(ma.Schema):
    
#validations
    type = fields.String(required = True, validate=OneOf(VALID_TYPES, error= f'The Service must be of a one of the following {VALID_TYPES}'))
    price = fields.String(required=True, validate=OneOf(VALID_PRICES, error= f'Price entered for service must be one of {VALID_PRICES}'))



    class Meta:
        fields = ('id', 'type', 'price')
        ordered = True