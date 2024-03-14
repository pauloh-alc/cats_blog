from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from dotenv import load_dotenv
from sqlalchemy.exc import ProgrammingError


load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# create the database
db = SQLAlchemy(app)

# starting the login
login_manager = LoginManager(app)

from app import models

try:
    with app.app_context():
        db.create_all()
except ProgrammingError:
    pass


from app import routes

if __name__ == '__main__':
    app.run(debug=True, port=5000)