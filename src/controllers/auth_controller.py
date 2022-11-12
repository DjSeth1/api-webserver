from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import timedelta
from models.user import User
from schemas.user_schema import UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

auth_bp = Blueprint('auth', __name__, url_prefix = '/auth')




@auth_bp.route('/register/', methods = ['POST'])
def auth_register():
    data = UserSchema().load(request.json)
    try:
        user = User(
            email = data['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
            f_name = data.get('f_name'),
            l_name = data.get('l_name'),
            phone = data.get('phone')
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
        return {'email': user.email, 'token': token, 'is_admin': user.is_admin}, 308
    else:
        return {'error': 'Invalid email or password'}, 401






