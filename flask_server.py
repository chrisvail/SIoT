from flask import Flask, request
import json
from policy import get_actions, get_control_policy
from system import build_system
from time import sleep

app = Flask(__name__)


@app.route('/log_data', methods=['POST'])
def log_data():
    data = request.json

    device = data["device_id"]

    control_policy = get_control_policy(device)
    actions = get_actions(device)

    storage_queue.put(data)

    return json.dumps({"action":actions, "policy":control_policy})

@app.route('/test_esp', methods=['POST'])
def test_esp():
    data = request.json
    print(data)

    return json.dumps({"action":"None", "policy":"None"})

if __name__ == '__main__':

    storage_queue = build_system()

    app.run(debug=True, host="0.0.0.0")