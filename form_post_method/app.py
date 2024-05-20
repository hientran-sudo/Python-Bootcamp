from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html") 

@app.route("/login", methods=["POST"])
def received_data():
  fname = request.form["fname"]
  lname = request.form["lname"]
  return f"First name: {fname}, Last name: {lname}"

if __name__ == "__main__":
  app.run(debug=True)
