from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from app.config.db import app_config

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from app.routes.alumno_routes import alumno_routes
    from app.routes.docente_routes import docente_routes
    from app.routes.main_routes import main_routes
    from app.routes.usuario_routes import usuario_routes

    app.register_blueprint(alumno_routes, url_prefix='/alumno')
    app.register_blueprint(docente_routes, url_prefix='/docente')
    app.register_blueprint(usuario_routes, url_prefix='/usuario')
    app.register_blueprint(main_routes, url_prefix='/')

    return app
