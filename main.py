import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port=port)
    #app.run(debug=True)
