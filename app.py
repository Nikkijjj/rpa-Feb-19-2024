from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
  return (render_template("index.html"))

@app.route("/main", methods=["GET","POST"])
def main():
  r = request.form.get("r")
  return (render_template("main.html", r=r))

@app.route("/image_gpt", methods=["GET","POST"])
def main():
  return (render_template("image_gpt.html"))

if __name__ == "__main__":
  app.run()
