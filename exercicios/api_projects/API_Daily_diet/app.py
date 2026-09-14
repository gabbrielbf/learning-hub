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

