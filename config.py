import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:vE1lyUShe8iqdnWwCY1MEmpXq9sG4P5T@dpg-cv99j4hc1ekc73e5l4u0-a.singapore-postgres.render.com/db_hztz')

