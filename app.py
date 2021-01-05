"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
app.py

app.py starts the application
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from flask import Flask

app = Flask(__name__)

from src.views import *

if __name__ == '__main__':
    app.run(use_reloader=True, host='0.0.0.0', port='8080')