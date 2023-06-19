from werkzeug.security import check_password_hash
from app.models.usuario import Usuario


def authenticate(username, password): # pylint: disable=missing-docstring
    user = Usuario.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return user
    return None
