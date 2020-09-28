from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_mail import Mail


db = SQLAlchemy()

mail = Mail()

def create_app(config_name):
    app = Flask(__name__)

    
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    


    # Initializing flask extensions
    db.init_app(app)
    mail.init_app(app)

    # Registering the blueprint
    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    return app
