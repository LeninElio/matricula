import os
from app import create_app
from flask import jsonify

app = create_app(os.getenv('FLASK_ENV', 'development'))


@app.errorhandler(404)
def page_not_found(e):
    mensaje = {'error': 'Página no encontrada.'}
    return jsonify(mensaje), 404


if __name__ == '__main__':
    app.run()
