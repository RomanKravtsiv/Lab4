from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/api/v1/hello-world-7")
    def hello():
        return "Hello World 7"

    return app
