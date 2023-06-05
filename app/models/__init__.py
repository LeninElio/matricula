from app.models.alumno import AlumnoSchema
from app.models.docente import DocenteSchema
from app.models.usuario import UsuarioSchema


usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
alumno_schema = AlumnoSchema()
alumnos_schema = AlumnoSchema(many=True)
docente_schema = DocenteSchema()
docentes_schema = DocenteSchema(many=True)
