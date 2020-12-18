from flask import Flask
from blueprints import blueprint

def db_error():
    return ({"code":500,"type":"DATABASE_ERROR"})

app = Flask(__name__)

app.register_blueprint(blueprint,url_prefix="/reiting")

#app.register_error_handler(Exception, db_error)

if __name__ == '__main__':
    app.run(debug = True)