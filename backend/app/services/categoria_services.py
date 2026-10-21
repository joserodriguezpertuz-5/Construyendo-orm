from flask import jsonify, request, abort
from app.models import Categoria, Producto, db

# LISTAR CATEGORIAS
def categoria_list():
    categorias = db.session.execute(
        db.select(Categoria)
    ).scalars().all()

    return jsonify([c.to_dict() for c in categorias]), 200

# DETALLE CATEGORIA
def categoria_detail(categoria_id):
    categoria = db.session.get(Categoria, categoria_id)

    if not categoria:
        abort(404, description= "Categoria no encontrada")
    return jsonify(categoria.to_dict()), 200

# CREAR CATEGORIA
def categoria_add():
    data = request.get_json()

    if not data:
        abort(400, description="No se recibio informacion en formato JSON")

    if "nombre" not in data:
        abort(400, description="El campo nombre es obligatorio")

    nueva_categoria = Categoria(
            categoria_nombre=data["nombre"],
            descripcion=data.get("descripcion")
    )

    db.session.add(nueva_categoria)
    db.session.commit()

    return jsonify(nueva_categoria.to_dict()), 201

# ACTUALIZAR CATEGORIA
def categoria_update(categoria_id):
    data = request.get_json()

    if not data:
        abort(400, description="No se recibio informacion en formato JSON")
    categoria = db.session.get(Categoria, categoria_id)

    if not categoria:
        abort(404, description="Categoria no encontrada")

    categoria.categoria_nombre = data.get("nombre", categoria.categoria_nombre)
    categoria.descripcion = data.get("descripcion", categoria.descripcion)

    db.session.commit()

    return jsonify(categoria.to_dict()), 200

# ELIMINAR CATEGORIA
def categoria_delete(categoria_id):
    categoria = db.session.get(Categoria, categoria_id)

    if not categoria:
        abort(404, description="Categoria no encontrada")

    # Validar que no tenga productos asociados
    tiene_productos = db.session.execute(
        db.select(Producto).where(Producto.categoria_id == categoria_id).limit(1)
    ).scalars().first()

    if tiene_productos:
        abort(409, description="No se puede eliminar: la categoria tiene productos asociados")

    db.session.delete(categoria)
    db.session.commit()

    return jsonify({"mensaje": "Categoria eliminada correctamente"}), 200


        

    