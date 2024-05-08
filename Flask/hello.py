from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

# tell ternminal by exporting the FLASK_APP environment variable:
# $ export FLASK_APP = hello.py (in Mac)
# $ set FLASK_APP = hello.py (in Windows)
# flask run
