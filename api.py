import os
import json
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def api_root():
    return "Stephen's Slack Macros. Welcome!"


@app.route('/macros/rofl')
def rofl():
    data = {
        "response_type": "in_channel",
        "text": ":slightly_smiling_face: :upside_down_face: :slightly_smiling_face: :upside_down_face: :slightly_smiling_face: :upside_down_face: :slightly_smiling_face:"
    }
    return jsonify(**data)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)