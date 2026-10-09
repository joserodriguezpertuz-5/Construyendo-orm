from flask import Blueprint
from flasgger import swag_from
from app.services import (
    categoria_list,
    categoria_detail,
    categoria_add,
    categoria_update,
    categoria_delete
)

categoria_bp = Blueprint("categorias", __name__)

# LISTAR CATEGORIAS
@swag_from({
    "summary": "Consulta general de categorias",
    "responses": {
        200: {"description": "Lista de categorias"},
        404: {"description": "No se encontraron categorias"}
    }
})
@categoria_bp.route("/categorias", methods=["GET"])
def get_categoria_list():
    return categoria_list()

# DETALLE CATEGORIA
@swag_from({
    "summary": "Consulta individual de categoria",
    "parameters": [
        {
            "name": "categoria_id",
            "in": "path",
            "type": "intenger",
            "required": True,
            "descripcion": "ID de la categoria",
            "example": 1
        }
    ],
    "responses": {
        200: {"description": "Detalle de categoria"},
        404: {"description": "caregoria no encontrada"}
    }
})
@categoria_bp.route("/categorias/<int:categoria_id>", methods=["GET"])
def get_categoria_detail(categoria_id):
    return categoria_detail(categoria_id)

# CREAR CATEGORIA
@swag_from({
    "summary": "Registro de categoria",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "required": ["nombre"],
                "properties": {
                    "nombre": {"type": "string", "example": "Electronica"},
                    "descripcion": {"type": "string", "example": "Peoductos electronicos"}
                }
            }
        }
    ],
    "responses": {
        201:{"description": "Categoria creada correctamente"},
        400: {"description": "Error en el registro"}
    }
})
@categoria_bp.route("/categorias", methods=["POST"])
def get_categoria_add():
    return categoria_add()

# ACTUALIZAR CATEGORIA 
@categoria_bp.route("/categorias/<int:categoria_id>", methods=["PUT"]) 
def get_categoria_update(categoria_id): 
    return categoria_update(categoria_id) 

# ELIMINAR CATEGORIA 
@categoria_bp.route("/categorias/<int:categoria_id>", methods=["DELETE"]) 
def get_categoria_delete(categoria_id): 
    return categoria_delete(categoria_id)

    