#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_is(text):
    return "C {}".format(text.replace('_', ' '))


app.run(host='0.0.0.0', port=5000)
