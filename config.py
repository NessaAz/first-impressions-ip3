import os



class Config:
    '''
    Parent class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class ProdConfig:
    '''
    Child to Config class
    '''
    pass

class DevConfig:
    '''
    Child to Config class
    '''
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}