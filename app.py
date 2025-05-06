import os
from flask import Flask
from backend.base_de_datos import db, init_models  

from routes.authentication.login import login
from routes.authentication.olvidado_contraseña import olvidado_contraseña
from routes.authentication.registro import registro
from routes.authentication.restablecer_contraseña import restablecer_contraseña
from routes.home import home

app = Flask(__name__)

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')


app.secret_key = os.urandom(24)  


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/tienda_online'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_models(app)  



app.add_url_rule('/', 'home', home)
app.add_url_rule('/login', 'login', login, methods=["GET", "POST"])
app.add_url_rule('/registro', 'registro', registro, methods=["GET", "POST"])
app.add_url_rule('/olvidado_contraseña', 'olvidado_contraseña', olvidado_contraseña, methods=["GET", "POST"])
app.add_url_rule('/restablecer_contraseña/<token>', 'restablecer_contraseña', restablecer_contraseña, methods=["GET", "POST"])

if __name__ == '__main__':
    app.run(debug=True)
