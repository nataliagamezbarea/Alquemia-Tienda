# backend/Modelos.py

# Se importan los módulos necesarios para trabajar con SQLAlchemy y Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import MetaData

# Se crea la instancia de SQLAlchemy sin pasarle la app por ahora
db = SQLAlchemy()

# Se crea un objeto metadata que se usará para reflejar las tablas existentes en la base de datos
metadata = MetaData()

# Se define la base para la automapeo, usando la metadata creada
Base = automap_base(metadata=metadata)

# Esta función se llama desde la app principal para inicializar los modelos
def init_models(app):
    # Se registra la app con SQLAlchemy
    db.init_app(app)
    with app.app_context():
        # Se reflejan solo las tablas necesarias desde la base de datos
        metadata.reflect(bind=db.engine, only=["usuarios"])  # Se puede quitar "only" para reflejar todas las tablas
        # Se preparan las clases automapeadas
        Base.prepare()

# Devuelve los nombres de las tablas reflejadas
def obtener_tablas():
    return list(Base.classes.keys())

# Devuelve la clase correspondiente a una tabla específica
def obtener_tabla(nombre):
    return Base.classes[nombre]
