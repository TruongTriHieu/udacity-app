"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config.from_object(Config)

# Cấu hình logging
if not app.debug:
    # Setup file handler for logging
    file_handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    app.logger.addHandler(file_handler)

# Setup console handler for logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
app.logger.addHandler(console_handler)

# Đặt mức độ logging cho ứng dụng
app.logger.setLevel(logging.INFO)

# Cấu hình Flask extensions
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views