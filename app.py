from flask import Flask

from routes.home import home

app = Flask(__name__)

app.add_url_rule('/', 'home', home)

if __name__ == '__main__':
    app.run()
