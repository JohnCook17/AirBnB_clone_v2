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

    @app.route('/cities_by_states')
    def city_list():
        if getenv("HBNB_TYPE_STORAGE") == "db":
            cities = list(storage.all("State").values())
        else:
            cities = State.cities()
        return render_template('8-cities_by_states.html', var=cities)

    app.run(host='0.0.0.0', port=5000)
