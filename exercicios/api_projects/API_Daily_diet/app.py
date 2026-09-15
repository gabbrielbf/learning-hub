from flask import Flask, request, jsonify
from models.user import User
from models.meal import Meal
from database import db
from flask_login import (
    LoginManager,
    login_user,
    current_user,
    logout_user,
    login_required
)
import bcrypt
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3307/daily-diet'

login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)

# Criando tabelas caso as mesmas não existam
with app.app_context():
    db.create_all()

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# ==========
# LOGIN
# ==========
@app.route('/login', methodos=['POST'])
def login():

    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.checkpw(
            str.encode(password),
            str.encode(user.password)
        ):
            login_user(user)

            return jsonify({
                'message': 'User authenticated successfully'
                })
        
    return ({
        'message': 'Invalid credentials'
    }), 404

# ==========
# LOGOUT
# ==========
app.route('/logout', methods=['GET'])
@login_required
def logout():

    logout_user()

    return jsonify({
        'message': 'Logout successful'
    })

# =============
# CREATE USER
# =============
@app.route('/user', methods=['POST'])
def create_user():

    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:

        hashed_password = bcrypt.hashpw(
            str.encode(password),
            bcrypt.gensalt()
        )

        user = User(
            username=username,
            password=hashed_password,
            role='user'
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({
            'message': 'User registred successfully'
        })

    return jsonify({
        'message': 'Invalid credentials'
    }), 401



if __name__ == '__main__':
    app.run()