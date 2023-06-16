"""
Este módulo define el modelo y el esquema para la entidad Alumno.
"""

from marshmallow_sqlalchemy import fields
from app import db, ma
from .usuario import Usuario


class Alumno(db.Model):
    """
    Define la tabla Alumno en la base de datos.
    """
    __tablename__ = 'alumno'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship(Usuario, backref='alumno')


class AlumnoSchema(ma.SQLAlchemySchema):
    """
    Define el esquema para serializar y deserializar instancias de Alumno.
    """
    class Meta:
        model = Alumno
        # exclude = ('id',)
        # ordered = False

    id = ma.auto_field()
    id_usuario = ma.auto_field()
    usuario = fields.Nested('UsuarioSchema')
