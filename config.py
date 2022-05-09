import os



class Config:
    '''
    Parent class
    '''
    pass

class ProdConfig:
    '''
    Child to Config class
    '''
    

class DevConfig:
    '''
    Child to Config class
    '''
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}