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

# =============
# CREATE MEAL
# =============
app.route('/meal', methods=['POST'])
@login_required
def create_meal():

    data = request.json

    name = data.get('name')
    description = data.get('description')
    date_time = data.get('date_time')
    is_on_diet = data.get('is_on_diet')

    if (name and description # <- Conferindo se todos os campos estão preenchidos corretamente 
        and date_time is not None 
        and is_on_diet is not None):

        # Conferindo se o formato amazenado na variavel é o formato padrão mundial
        try:
            date_time = datetime.fromisoformat(date_time)
        except ValueError:
            return jsonify({
                'message': 'Invalid date format'
            }), 400

        meal = Meal(
            name=name,
            description=description,
            date_time=date_time,
            is_on_diet=is_on_diet,
            user_id=current_user.id
        )

        db.session.add(meal)
        db.session.commit()

        return jsonify({
            'message': 'Meal registered successfully'
        }), 201

    return jsonify({
        'message': 'Invalid meal data'
    }), 400

# =============
# LIST MEALS
# =============
app.route('/meals', methods=['GET'])
@login_required
def read_meals():

    meals = Meal.query.filter_by(
        user_id=current_user.id
    ).all()

    return jsonify([
        {
            'id': meal.id,
            'name': meal.name,
            'description': meal.description,
            'date_time': meal.date_time.isoformat(),
            'is_on_diet': meal.is_on_diet
        }
        for meal in meals
    ])

# =============
# READ MEAL
# =============
app.route('/meal/<int:id_meal>', methods=['GET'])
@login_required
def read_meal(id_meal):

    meal = Meal.query.get(id_meal)

    if not meal:
        return jsonify({
            'message': 'Meal not found'
        }), 404

    if meal.user_id != current_user.id:
        return jsonify({
            'message': 'Operation not supported'
        }), 403

    return jsonify({
        'id': meal.id,
        'name': meal.name,
        'description': meal.description,
        'date_time': meal.date_time.isoformat(),
        'is_on_diet': meal.is_on_diet
    })

# =============
# UPDATE MEAL
# =============
app.route('/meal/<int:id_meal>', methods=['PUT'])
@login_required
def update_meal(id_meal):

    data = request.json

    meal = Meal.query.get(id_meal)

    if not meal:
        return jsonify({
            'message': 'Meal not found'
        }), 404

    if meal.user_id != current_user.id:
        return jsonify({
            'message': 'Operation not supported'
        }), 403

    

if __name__ == '__main__':
    app.run()