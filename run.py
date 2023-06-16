import os
from flask import jsonify
from app import create_app

app = create_app(os.getenv('FLASK_ENV', 'development'))


@app.errorhandler(404)
def page_not_found(e):
    """
    Esta función devuelve un mensaje JSON con un error de "página no encontrada" y un código
    de estado 404.
    
    :param e: El parámetro "e" es un objeto de excepción que se pasa a la función cuando no
    se encuentra una página. Contiene información sobre el error que ocurrió
    :return: Un objeto JSON con el mensaje "Página no encontrada" y un código de estado de 
    404 (página no encontrada).
    """
    mensaje = {'error': 'Página no encontrada.'}
    return jsonify(mensaje), 404


if __name__ == '__main__':
    app.run()
