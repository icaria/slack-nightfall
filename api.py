import os
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/macros/rofl')
def rofl():
    return ':slightly_smiling_face: :upside_down_face: :slightly_smiling_face: :upside_down_face: :slightly_smiling_face: :upside_down_face: :slightly_smiling_face:'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)