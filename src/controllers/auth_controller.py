from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import timedelta
from models.user import User
from schemas.user_schema import UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

auth_bp = Blueprint('auth', __name__, url_prefix = '/auth')

#get users (barber/admin only allowed to view all users)
@auth_bp.route('/users/', methods = ['GET'])
def get_user():
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many = True, exclude = ['password']).dump(users)


@auth_bp.route('/register/', methods = ['POST'])
def auth_register():
    try:
        user = User(
            email = request.json['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
            f_name = request.json.get('f_name'),
            l_name = request.json.get('l_name'),
            phone = request.json.get('phone')
        )
        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {"error": 'Email is already in use, please use another email address'}, 409

@auth_bp.route('/login/', methods=['POST'])
def auth_login():
    stmt = db.select(User).filter_by(email=request.json['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        return {'email': user.email, 'token': token, 'is_admin': user.is_admin}
    else:
        return {'error': 'Invalid email or password'}, 401






