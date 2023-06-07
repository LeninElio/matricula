from app import db
from app.models.alumno import Alumno
from app.models import alumno_schema, alumnos_schema
from app.controllers.usuario_controller import UsuarioController


class AlumnoController:

    @staticmethod
    def crear(data):
        usuario = UsuarioController.crear(data)
        if usuario.get('error') is not None:
            return usuario

        else:
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
