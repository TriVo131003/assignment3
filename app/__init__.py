from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import redis

db = SQLAlchemy()
redis_client = None 

def create_app():
    global redis_client 

    app = Flask(__name__)
    app.config.from_object(Config)

    redis_client = redis.StrictRedis.from_url(Config.REDIS_URL, decode_responses=True, ssl=True)

    db.init_app(app)

    with app.app_context():
        from .routes import main_bp
        app.register_blueprint(main_bp)

        db.create_all()

    return app
