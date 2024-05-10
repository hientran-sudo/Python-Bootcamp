from flask import Flask
import random
app = Flask(__name__)

num = random.randint(0,9)

@app.route('/')
def home():
  return '<h1 style="text-align: center">Guess a Number between 0 and 9</h1>' \
         '<img src="https://cdn.vectorstock.com/i/2000v/27/65/donut-cartoon-nine-number-vector-29112765.avif" width="300" height="300"/>' 

@app.route("/<int:number>")
def guessing(number):
  if num > number:
    return "Too low"
  elif num < number:
    return "Too high"

if __name__ == "__main__":
  app.run(debug=True)
