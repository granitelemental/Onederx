from flask import Flask, request, jsonify

import config
from db import Data

app = Flask('API')
data = Data()


@app.route('/alarm', methods=["POST"])
def add_alarm():

    alarm = request.get_json()
    res = data.save(alarm)
    return {"status": "Ok", "data": res}, 200


@app.route('/alarm', methods=["GET"])
def get_active():
    res = data.get_active()
    return {"status": "Ok", "data": res}, 200


def start_app():
    app.run(host=config.API_HOST, port=config.API_PORT, debug=True)


if __name__ == "__main__":
    start_app()
