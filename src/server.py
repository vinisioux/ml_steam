from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from modules.games.routes import *

if __name__ == '__main__':
  app.run(debug=True)
