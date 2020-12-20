from flask import Flask
from blueprints import blueprint
from flask_jwt_extended import JWTManager

def db_error():
    return jsonify({
        "code":500,
        "type":"DATABASE_ERROR"
        })

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'JFGD23IUHI23G4IU3YG22G42H34HB2J4IG243IBBG4353HJK45GB3HJK53K5VBH3'
jwt = JWTManager(app)


app.register_blueprint(blueprint,url_prefix="/rating")

# app.register_error_handler(Exception, db_error)

if __name__ == '__main__':
    app.run(debug = True)