from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import redis
from app.thread import background_task

db = SQLAlchemy()
redis_client = None 

def create_app():
    global redis_client 

    app = Flask(__name__)
    app.config.from_object(Config)

    redis_client = redis.StrictRedis.from_url(Config.REDIS_URL, decode_responses=True)

    db.init_app(app)

    with app.app_context():
        from .routes import main_bp
        app.register_blueprint(main_bp)

        db.create_all()

        from seeder import load_data
        load_data()

        background_task.start(app)

    return app
