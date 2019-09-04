#!/usr/bin/python3

if __name__ == "__main__":
    from os import getenv
    from models import storage
    from models.state import State
    from flask import Flask, render_template
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.teardown_appcontext
    def close_app(i=None):
        storage.close()

    @app.route('/states', defaults={'id': None})
    @app.route('/states/<id>')
    def states_by_name(id):
        states = list(storage.all("State").values())
        for state in states:
            if state.id == id:
                print (state.id)
                states = state
        return render_template('9-states.html', id=id, states=states)

    app.run(host='0.0.0.0', port=5000)
