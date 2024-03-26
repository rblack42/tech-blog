from flask import Flask


def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    register_blueprints(app)
    return app


def register_blueprints(app):
    from app.frontend import frontend_blueprint
    app.register_blueprint(frontend_blueprint)
