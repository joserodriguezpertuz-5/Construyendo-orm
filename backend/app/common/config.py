import pymysql

class Config:
    # Datos de conexion para MySQL (ajusta segun tus credenciales)
    USER = 'root'              # Usuario de MySQL
    PASSWORD = ''          #Contraseña de MySQL
    HOST = 'localhost'          # Host donde Corre MySQL (localhost por defecto)
    DATABASE = 'db_productos' # Nombre de la base de datos

    # URL de conexion para SQLALchemy usando el conector PyMySQL
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}'

    # Desactiva el rastreo de modificaciones para evitar advertencias
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    