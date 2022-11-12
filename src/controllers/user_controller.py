from flask import Blueprint, request
from init import db, bcrypt
from models.user import User
from schemas.user_schema import UserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError



user_bp = Blueprint('users', __name__ , url_prefix='/users')





@user_bp.route('/all_users/', methods = ['GET'])
@jwt_required()
def get_all_users():

    stmt = db.select(User).order_by(User.l_name)
    users = db.session.scalars(stmt)
    return UserSchema(many = True, exclude =['password']).dump(users)




#read one user( get user)
@user_bp.route('/<int:id>/', methods = ['GET'])
@jwt_required()
def get_one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude = ['password']).dump(user)
    else:
        return {'error': f' There is no user with id{id}.'}, 404



#update user info 
@user_bp.route('/<int:user_id>/', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_user(user_id):
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)

    if user:
        data = UserSchema().load(request.json)
        user.f_name = data['f_name'] or user.f_name
        user.l_name = data['l_name'] or user.l_name
        user.email = data['email'] or user.email
        user.password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8') or user.password
        user.phone = data['phone'] or user.phone

        db.session.commit()
        return {
            'success': 'You have updated your profile successfully',
            'user details': UserSchema().dump(user)
        }
    else:
        return {'error': 'User does not exist'}, 404


#delete a user 
@user_bp.route('/<int:user_id>/', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user_id = get_jwt_identity()

    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f' Your records with name {user.f_name} {user.l_name} were successfully deleted!'}
    else:
        return {'error': f'User not found with id {user_id}.'}, 404

