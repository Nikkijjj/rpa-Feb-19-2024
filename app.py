from flask import Flask, request, render_template
from flask import redirect, url_for
from openai import OpenAI
import replicate
import os
import time

os.environ["REPLICATE_API_TOKEN"] = "r8_LQBrEtBcljk7Z3uqYNGOIwUoiREHa4u3yeGyC"
openai_api_key = os.getenv("OPENAI_API_KEY")
model = OpenAI(api_key=openai_api_key)
app = Flask(__name__)

r = ""
first_time = 1


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/main", methods=["GET", "POST"])
def main():
    global r, first_time
    if first_time == 1:
        r = request.form.get("r")
        first_time = 0
    return render_template("main.html", r=r)


@app.route("/image_gpt", methods=["GET", "POST"])
def image_gpt():
    return render_template("image_gpt.html")


@app.route("/image_result", methods=["GET", "POST"])
def image_result():
    q = request.form.get("q")
    r = replicate.run("stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
                      input={"prompt": q})
    time.sleep(5)
    return render_template("image_result.html", r=r[0])


@app.route("/text_gpt", methods=["GET", "POST"])
def text_gpt():
    return render_template("text_gpt.html")


@app.route("/text_result", methods=["GET", "POST"])
def text_result():
    q = request.form.get("q")
    r = model.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": q
            }
        ]
    )
    time.sleep(5)
    return render_template("text_result.html", r=r.choices[0].message.content)

@app.route("/text_ntu", methods=["GET", "POST"])
def text_ntu():
    return render_template("text_ntu.html")

@app.route("/image_ntu", methods=["GET", "POST"])
def image_ntu():
    return render_template("image_ntu.html")

@app.route("/building_ntu", methods=["GET", "POST"])
def building_ntu():
    return render_template("building_ntu.html")

@app.route("/activities_ntu", methods=["GET", "POST"])
def activities_ntu():
    return render_template("activities_ntu.html")
    
@app.route("/website_ntu", methods=["GET", "POST"])
def website_ntu():
    if request.method == "POST":
        website_url = "https://www.ntu.edu.sg/"
        return redirect(website_url)

@app.route("/end", methods=["GET", "POST"])
def end():
    first_time = 1
    return render_template("end.html")


if __name__ == "__main__":
    app.run()
