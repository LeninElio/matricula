from app import db, ma


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    sexo = db.Column(db.Boolean())


class UsuarioSchema(ma.Schema):
    class Meta:
        # ordered = False
        # fields = ('id', 'nombre', 'email')
        fields = (
            'id', 'nombre', 'apellido_paterno',
            'apellido_materno', 'email',
            'username', 'sexo'
            )
