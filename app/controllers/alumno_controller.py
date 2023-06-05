from app import db
from app.models.alumno import Alumno
from app.models import alumno_schema, alumnos_schema


class AlumnoController:
    @staticmethod
    def create(data):
        alumno = Alumno(id_usuario=data['id_usuario'])
        db.session.add(alumno)
        db.session.commit()
        return alumno_schema.dump(alumno)

    @staticmethod
    def read():
        alumnos = Alumno.query.all()
        return alumnos_schema.dump(alumnos)

    @staticmethod
    def solo(id):
        alumno = Alumno.query.get(id)
        return alumno_schema.dump(alumno)
