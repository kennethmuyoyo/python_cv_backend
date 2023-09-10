from flask import Flask
from .user_management import user_bp
from .cv_operations import cv_bp
from .ai_services import ai_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite for simplicity

db = SQLAlchemy(app)

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(cv_bp, url_prefix='/cv')
app.register_blueprint(ai_bp, url_prefix='/ai')

from app import routes, models
