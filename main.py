from flask import Flask, make_response


def create_page():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "<h2>Main<h2>"

    @app.route('/api/v1/hello-world-12')
    def api_v1():
        return make_response("<h2>Hello World 12<h2>", 200)

    return app