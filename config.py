import os

class Config:
    '''
    General config parent class
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS= True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rita:p@localhost/blogapp'
    QUOTES_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    # email configs
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    '''
    Production config child class

    Args:
        Config: The parent config class with General config settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Testing config child class

    Args:
        Config: The parent config class with General config settings
    '''
    pass

class DevConfig(Config):
    '''
    Dev config child class

    Args:
        Config: The parent config class with General config settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://swbrsbtpjekbpl:14bb0b04a1ee865a85637609b38c7c89b38725dd293e38e940505cfc5513524a@ec2-54-83-33-14.compute-1.amazonaws.com:5432/d2h379tfijh9r4'


    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}




