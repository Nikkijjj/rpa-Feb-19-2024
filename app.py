# front part
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
  return (render_template("index.html"))

if __name__ == "_main_":
  app.run()
