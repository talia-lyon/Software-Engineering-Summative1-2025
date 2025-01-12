from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['DATABASE'] = 'data.db'

    from .routes import bp
    app.register_blueprint(bp)

    return app
