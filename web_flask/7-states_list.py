#!/usr/bin/python3

if __name__ == "__main__":
    from models import storage
    from flask import Flask, render_template
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.teardown_appcontext
    def close_app(i=None):
        storage.close()

    @app.route('/states_list')
    def state_list():
        states = list(storage.all("State").values())
        return render_template('7-states_list.html', var=states)

    app.run(host='0.0.0.0', port=5000)
