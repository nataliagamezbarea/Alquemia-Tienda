from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Esto configura tu aplicación de Flask, como que la base de datos 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/tienda_online'  # Conexión con MySQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Para que no me mande warnings

# Inicializamos la base de datos y SQLAlchemy
db = SQLAlchemy(app)
Base = automap_base()

with app.app_context():
    engine = db.engine  # El engine es como el motor de la base de datos
    Base.prepare(autoload_with=engine)  # Esto carga las tablas de la base de datos automáticamente

# Función para obtener todas las tablas disponibles (esto es como ver las carpetas en tu ordenador)
def obtener_tablas():
    with app.app_context():
        # Crear la sesión dentro de un context manager para asegurarse de que se cierre después de usarla
        session = Session(db.engine)
        tablas = list(Base.classes.keys())  # Aquí se devuelven los nombres de las tablas, como una lista
        session.close()  # Cierra la sesión después de usarla
        return tablas

# Función para obtener una tabla específica (como abrir una carpeta y ver lo que hay dentro)
def obtener_tabla(nombre):
    with app.app_context():
        session = Session(db.engine)
        tabla = Base.classes[nombre]  # Esto es como buscar una tabla por su nombre y devolverla
        session.close()  # Cierra la sesión después de usarla
        return tabla
