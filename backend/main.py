from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger

from app.models import db, Producto, Categoria, Entrada
from app.common import error_bp, Config
from app.controller import productos_bp, categoria_bp, entrada_bp

# Crear aplicacion 
app = Flask(__name__)

#Configuracion
app.config.from_object(Config)

# Inicializar extensiones
CORS(app)
swagger = Swagger(app)
db.init_app(app)

# Crear tablas automaticamente 
with app.app_context():
    db.create_all()

# Ruta raiz 
@app.route("/", methods=["GET"])
def home():
    """
    Ruta de prueba para verificar que la API este
    Funcionando

    """

    return jsonify({"mensaje": "API funcionamiento correctamente"}), 200

# Registrar blueprints
app.register_blueprint(error_bp)
app.register_blueprint(productos_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(entrada_bp)

if __name__ == "__main__":
   app.run(host="127.0.0.1", port=5000, debug=True)