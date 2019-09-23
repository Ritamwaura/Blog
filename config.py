import os

class Config:
    '''
    General config parent class
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS= True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://britneyritah2019@gmail.com123@localhost/blogapp'

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

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}




