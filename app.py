from flask import Flask
from routes.web import bp
from extensions import db
from models import User, Project, Skill, Article
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.register_blueprint(bp)

# Configuration Model
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Database init
db.init_app(app)

# Database Migration
migrate = Migrate(app, db)

# Cek jika lupa setting .env
if not app.config["SQLALCHEMY_DATABASE_URI"]:
    raise RuntimeError("Variable DB_URI is not setting yet in .env file!")

if __name__ == "__main__":
    app.run(debug=True)
