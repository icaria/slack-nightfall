from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/macros/rofl')
def rofl():
    return ':slightly_smiling_face: :upside_down_face: :slightly_smiling_face: :upside_down_face: :slightly_smiling_face: :upside_down_face: :slightly_smiling_face:'

if __name__ == '__main__':
    app.run()
