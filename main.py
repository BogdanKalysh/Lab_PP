from flask import Flask, make_response


def create_page():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Main page"

    @app.route('/api/v1/hello-world-12')
    def api_v1():
        return make_response("Hello World 12", 200)

    return app
