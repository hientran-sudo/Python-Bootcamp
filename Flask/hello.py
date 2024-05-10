from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/username/<name>/<int:number>')
def great(name):
  return 'Hello {name}. You're {number} yrs old!'


# tell ternminal by exporting the FLASK_APP environment variable:
# $ export FLASK_APP = hello.py (in Mac)
# $ set FLASK_APP = hello.py (in Windows)
# $ flask run
