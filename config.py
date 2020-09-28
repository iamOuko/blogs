
import os

class Config():

    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ouko:Nighthawk96@localhost/posts'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):  
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("postgres://jrttfmuvchdumw:cf486a8244688b4bf37b40787a70d72e95837e0016dfa40f5dc9404640e3ab33@ec2-3-218-112-22.compute-1.amazonaws.com:5432/d827trsdlsn5m7")
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ouko:Nighthawk96@localhost/posts_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ouko:Nighthawk96@localhost/posts'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}