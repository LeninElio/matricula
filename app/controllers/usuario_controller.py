from app import db
from werkzeug.security import generate_password_hash
from app.models.alumno import Usuario
from app.models import usuario_schema, usuarios_schema


class UsuarioController:

    @staticmethod
    def crear(data):
        correo = Usuario.query.filter_by(email=data['email']).first()
        username = Usuario.query.filter_by(username=data['username']).first()
        if correo:
            return {'error': 'El correo electrónico ya está en uso'}

        elif username:
            return {'error': 'El nombre de usuario ya está en uso'}

        else:
            usuario = Usuario(
                nombre=data['nombre'],
                apellido_paterno=data['apellido_paterno'],
                apellido_materno=data['apellido_materno'],
                email=data['email'],
                sexo=data['sexo'],
                username=data['username'],
                password=generate_password_hash(data['password'])
            )

            db.session.add(usuario)
            db.session.commit()
            return usuario_schema.dump(usuario)

    @staticmethod
    def usuarios_todos():
        usuarios = Usuario.query.all()
        return usuarios_schema.dump(usuarios)

    @staticmethod
    def un_usuario(id):
        usuario = Usuario.query.get(id)
        return usuario_schema.dump(usuario)

    @staticmethod
    def eliminar_usuario(id):
        usuario = Usuario.query.get(id)
        db.session.delete(usuario)
        db.session.commit()
