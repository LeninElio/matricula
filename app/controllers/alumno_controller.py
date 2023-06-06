from app import db
from app.models.alumno import Alumno
from app.models.usuario import Usuario
from app.models import alumno_schema, alumnos_schema
from app.controllers.usuario_controller import UsuarioController


class AlumnoController:

    @staticmethod
    def crear(data):
        usuario = Usuario.query.filter_by(email=data['email']).first()
        if usuario:
            return {"Error": "El correo ya existe."}

        else:
            usuario_data = {
                'nombre': data['nombre'],
                'email': data['email']
            }
            usuario = UsuarioController.crear(usuario_data)
            alumno = Alumno(id_usuario=usuario['id'])
            db.session.add(alumno)
            db.session.commit()
            return alumno_schema.dump(alumno)

    @staticmethod
    def alumnos_todos():
        alumnos = Alumno.query.all()
        return alumnos_schema.dump(alumnos)

    @staticmethod
    def un_alumno(id):
        alumno = Alumno.query.get(id)
        return alumno_schema.dump(alumno)

    @staticmethod
    def eliminar_alumno(id):
        alumno = Alumno.query.get(id)
        db.session.delete(alumno)
        db.session.commit()
