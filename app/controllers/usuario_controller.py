from app import db
from werkzeug.security import generate_password_hash
from app.models.alumno import Usuario
from app.models import usuario_schema, usuarios_schema
from app.utils import validacion
from jsonschema import validate
from jsonschema.exceptions import ValidationError


class UsuarioController:

    @staticmethod
    def crear(data):
        try:
            validate(instance=data, schema=validacion.schema)
        except ValidationError:
            return {'error': 'Hay valores no admitidos en los datos.'}
        except Exception as e:
            return e

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

    @staticmethod
    def actualizar_usuario(id, data):
        try:
            validate(instance=data, schema=validacion.schema)
        except ValidationError:
            return {'error': 'Hay valores no admitidos en los datos.'}
        except Exception as e:
            return e

        usuario = Usuario.query.get(id)
        if 'username' in data and data['username'] != usuario.username:
            username = Usuario.query.filter_by(username=data['username']).first()
            if username:
                return {'error': 'El nombre de usuario ya esta en uso.'}

        for key in data:
            if key != 'password':
                setattr(usuario, key, data[key])
        db.session.commit()
        return usuario.to_dict()
