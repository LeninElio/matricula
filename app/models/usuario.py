"""
Este módulo define el modelo y el esquema para la entidad Alumno.
"""

from app import db, ma


class Usuario(db.Model):
    """
    Define la tabla Usuario en la base de datos.
    """
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    sexo = db.Column(db.Boolean())
    is_admin = db.Column(db.Boolean())

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido_paterno': self.apellido_paterno,
            'apellido_materno': self.apellido_materno,
            'email': self.email,
            'username': self.username,
            # 'password': self.password,
            'sexo': self.sexo
        }


class UsuarioSchema(ma.Schema):
    """
    Define el esquema para serializar y deserializar instancias de Usuario.
    """
    class Meta:
        # ordered = False
        # fields = ('id', 'nombre', 'email')
        fields = (
            'id', 'nombre', 'apellido_paterno',
            'apellido_materno', 'email',
            'username', 'sexo'
            )
