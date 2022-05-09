from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

#Definitions
bootstrap = Bootstrap()

#initializing application
def create_app(config_name):
    app = Flask(__name__ )
    
    #Creating the app configurations
    app.config.from_object (config_options[config_name])
    
    # Initializing Flask Extensions
    bootstrap.init_app(app)
    
    
    return app