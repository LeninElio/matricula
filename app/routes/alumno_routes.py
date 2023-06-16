"""
Modulo para el manejo de las rutas del alumno.
"""

from flask import Blueprint, request, jsonify
from app.models.alumno import Alumno
from app.controllers.alumno_controller import AlumnoController

alumno_routes = Blueprint('alumno_routes', __name__)


@alumno_routes.route('/create', methods=['POST'])
def crear():
    """
    Esta función crea un nuevo registro de estudiante utilizando datos de una solicitud 
    JSON y devuelve el registro creado como una respuesta JSON.
    :return: La función `crear()` devuelve una respuesta JSON que contiene los datos de un objeto de
    estudiante (alumno) recién creado.
    """
    data = request.json
    alumno = AlumnoController.crear(data)
    return jsonify(alumno)


@alumno_routes.route('/', methods=['GET'])
def alumnos_todos():
    """
    Esta función recupera a todos los alumnos y los devuelve como un objeto JSON.
    :return: La función `alumnos_todos()` está devolviendo una representación JSON de todos los
    estudiantes en la base de datos.
    """
    alumnos = AlumnoController.alumnos_todos()
    return jsonify(alumnos)


@alumno_routes.route('/<int:id_alumno>', methods=['GET'])
def un_alumno(id_alumno):
    """
    Esta función recupera la información de un estudiante por su ID y la devuelve en formato JSON.
    
    :param id_alumno: El parámetro "id_alumno" es una variable que representa el identificador
    único de un alumno en un sistema. Se usa como entrada a la función "un_alumno" que recupera
    la información del estudiante con la identificación dada del "AlumnoController".
    :return: una representación JSON del objeto de estudiante utilizando el ID del estudiante.
    """
    alumno = AlumnoController.un_alumno(id_alumno)
    return jsonify(alumno)


@alumno_routes.route('/<int:id>', methods=['DELETE'])
def eliminar_alumno(id_alumno):
    """
    Esta función elimina a un estudiante de la base de datos y devuelve un mensaje que indica si la
    eliminación fue exitosa o no.
    
    :param id_alumno: El parámetro id_alumno es el identificador único del alumno que debe 
    eliminarse de la base de datos.
    :return: Si no se encuentra el alumno, se devuelve una respuesta JSON con un mensaje de 
    error y un código de estado 404. Si se encuentra el alumno y se elimina con éxito, se devuelve 
    una respuesta JSON con un mensaje de éxito y un código de estado 200.
    """
    alumno = Alumno.query.get(id_alumno)
    if alumno is None:
        return jsonify({'error': 'Alumno no encontrado.'}), 404
    AlumnoController.eliminar_alumno(id_alumno)
    return jsonify({'message': 'Alumno eliminado.'}), 200


@alumno_routes.route('/<int:id>', methods=['PUT'])
def actualizar_alumno(id_alumno):
    """
    Esta función actualiza la información de un estudiante y devuelve los datos actualizados del
    estudiante.
    
    :param id_alumno: El parámetro `id_alumno` es el ID del estudiante que necesita ser actualizado.
    :return: Si hay un error, la función devuelve un diccionario con un mensaje de error. En
    caso contrario, devuelve el resultado de llamar al método `un_alumno` de la clase 
    `AlumnoController` con el `id` del usuario asociado al alumno actualizado.
    """
    data = request.get_json()
    alumno = AlumnoController.actualizar_alumno(id_alumno, data)
    if alumno.get('error') is not None:
        return alumno

    id_usuario = Alumno.query.filter_by(id_usuario=alumno['id']).first()
    return AlumnoController.un_alumno(id_usuario.id)
