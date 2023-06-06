from app import db
from app.models.alumno import Usuario
from app.models import usuario_schema, usuarios_schema


class UsuarioController:

    @staticmethod
    def create(data):
        usuario = Usuario(
            nombre=data['nombre'],
            email=data['email']
        )
        db.session.add(usuario)
        db.session.commit()
        return usuario_schema.dump(usuario)

    @staticmethod
    def read():
        alumnos = Usuario.query.all()
        return usuarios_schema.dump(alumnos)
