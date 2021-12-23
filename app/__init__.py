from flask import Flask
import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    register_web(app)
    return app

def register_web(app):
    from app.web import web
    app.register_blueprint(web)
