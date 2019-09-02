#!/usr/bin/python3
if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    app.url_map.strict_slashes = False


    @app.route('/')
    def hello_HBNB():
        return "Hello HBNB!"


    app.run(host='0.0.0.0', port=5000)
