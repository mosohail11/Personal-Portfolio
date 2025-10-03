from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=False)

    # Blueprints
    from .main import main_bp
    app.register_blueprint(main_bp)

    return app
