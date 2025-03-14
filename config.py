import os

class Config:
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:strongpassword@localhost:5432/exam_db')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:vE1lyUShe8iqdnWwCY1MEmpXq9sG4P5T@dpg-cv99j4hc1ekc73e5l4u0-a.singapore-postgres.render.com/db_hztz')
    REDIS_URL = os.getenv("REDIS_URL", "rediss://redis-cache-c7rh.onrender.com:6379")