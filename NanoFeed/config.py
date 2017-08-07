class Config(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/nanofeed'

class DevelopmentConfig(Config):
    DEBUG = True