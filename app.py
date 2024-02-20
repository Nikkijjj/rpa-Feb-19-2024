from flask import Flask,request,render_template

app = Flask(__name__)

r = ""
first_time = 1

@app.route("/",methods=["GET","POST"])
def index():
  return (render_template("index.html"))

@app.route("/main", methods=["GET","POST"])
def main():
  global r, first_time
  if first_time==1:
    r = request.form.get("r")
    first_time=0
  return (render_template("main.html", r=r))

@app.route("/image_gpt", methods=["GET","POST"])
def image_gpt():
  return (render_template("image_gpt.html"))

@app.route("/end", methods=["GET","POST"])
def end():
  global first_time=1
  return (render_template("end.html"))


if __name__ == "__main__":
  app.run()
