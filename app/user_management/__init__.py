from flask import Blueprint

user_bp = Blueprint('user_bp', __name__)

# Explicitly import the routes after Blueprint is defined to avoid circular dependencies
from .routes import *
