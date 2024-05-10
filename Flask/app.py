from flask import Flask
app = Flask(__name__)

def bye():
  return "Bye!"

@app.route('/')
def hello_world():
  return '<h1 style="text-align: center">Hello World!</h1>' \
         '<p> Paragraph </p>' 

@app.route('/username/<name>/<int:number>')
def great(name):
  return "Hello {name}. You're {number} yrs old!"
