from flask import Blueprint, request
from init import db, bcrypt
from models.user import User
from models.barber import Barber
from schemas.user_schema import UserSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from main import unauthorized


user_bp = Blueprint('users', __name__ , url_prefix='/users')


#create a user
user_bp.route('/', methods=['POST'])
#@jwt_required()
def create_user():
    data = UserSchema().load(request.json)

    user = User(
        f_name = data['f_name'],
        l_name = data['l_name'],
        email = data['email'],
        password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
        phone = data['phone']

    )

    db.session.add(user)
    db.session.commit()
    return UserSchema(exclude = ['password']).dump(user), 201




#read all users (get users) - barbers only+ isAdmin required (might be better in barber routes) #come back to this to see how to check if user is barber.
@user_bp.route('/')
#@jwt_required
def get_all_users():
    try:
       if Barber.is_admin == True:
        stmt = db.select(User).order_by(User.l_name)
        users = db.session.scalars(stmt)
        return UserSchema(many = True, exclude =['password']).dump(users)
    except:
        return unauthorized, 401



#read one user( get user)
@user_bp.route('/<int:id>', methods = ['GET'])
def get_one_user():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude = ['password']).dump(user)
    else:
        return {'error': f' There is no user with id{user_id}.'}, 404



#update user info 
@user_bp.route('/update/', methods = ['PUT', 'PATCH'])
@jwt_required
def update_user():
    stmt = db.select(User).filter_by(id = get_jwt_identity())
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
@user_bp.route('/delete/', methods=['DELETE'])
@jwt_required
def delete_user():
    stmt = db.select(User).filter_by(id = get_jwt_identity)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f' Your records with name "{user.first_name} {user.last_name}" were successfully deleted!'}
    else:
        {'error': 'User does not exist'}, 404

