from flask import Flask
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'
    app.config['UPLOAD_FOLDER'] = 'uploads'

    app.register_blueprint(bp)

    return app
