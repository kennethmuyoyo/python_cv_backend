from flask import request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from . import user_bp
from app.models import User
from app import db  


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        session['user_id'] = user.id
        return jsonify({"message": "Logged in"}), 200
    return jsonify({"message": "Bad credentials"}), 401