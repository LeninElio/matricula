schema = {
    "type": "object",
    "properties": {
        "nombre": {
            "type": "string",
            "pattern": "^[a-zA-Z ]+$"
            },
        "apellido_materno": {
            "type": "string",
            "pattern": "^[a-zA-Z ]+$"
            },
        "apellido_paterno": {
            "type": "string",
            "pattern": "^[a-zA-Z ]+$"
            },
        "sexo": {
            "type": "integer",
            "enum": [0, 1]
            },
        "email": {
            "type": "string",
            "pattern": r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
            },
        "username": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_]+$"
            }
        # "password": {
        #     "type": "string"
        #     }
    },
    # "required": ["nombre", "apellido_materno"]
    "required": []
}
