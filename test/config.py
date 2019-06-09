import os

class Config:
    SECRET_KEY = "secret key"
    UPLOAD_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:zq@localhost:3306/helloworld"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
