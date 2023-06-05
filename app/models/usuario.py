from app import db, ma


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)


class UsuarioSchema(ma.Schema):
    class Meta:
        # ordered = False
        fields = ('id', 'nombre', 'email')
        # fields = ('nombre', 'email')
