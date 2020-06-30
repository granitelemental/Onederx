from flask import Flask, request, jsonify

import config
from db import Data

app = Flask('API')
data = Data()

@app.route('/alarm', methods=["POST"])
def add_alarm():

    alarm = request.get_json()
    return data.save(alarm)


@app.route('/alarm', methods=["GET"])
def get_active_alarms():
    return data.get_active()


@app.route("/db", methods=["DELETE"])
def clear_db():
    return data.clear_db()


def start_app():
    # app.run(host="0.0.0.0", port=8080 , debug=True)
    app.run(host=config.API_HOST, port=config.API_PORT , debug=True)

if __name__ == "__main__":
    start_app()
