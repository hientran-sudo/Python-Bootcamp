from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html") 

@app.route("/add", methods=["POST"])
def add():
  return render_template("add.html") 

@app.route("/login", methods=["POST","GET"])
def received_data():
  if request.method == "POST":
    f = open("list.txt","a")
    fname = request.form["fname"]
    lname = request.form["lname"]
    f.write(f"{fname} {lname}\n")
    f.close()
    return render_template("login.html")
  else:
    f = open("list.txt","r")
    return f.readlines()
  

if __name__ == "__main__":
  app.run(debug=True)
