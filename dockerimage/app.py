import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    version = '--not present--'
    if 'SERVICE_REVISION' in os.environ.keys():
        version = os.environ['SERVICE_REVISION']
    return 'Flask Dockerized SERVICE_REVISION: ' + version

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')