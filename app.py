from flask import Flask,render_template,request,abort
from http import HTTPStatus

from helpers import clone

app = Flask(__name__,template_folder="templates",static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create",methods=["POST"])
def create():
    url = request.form.get("url")
    try:
        dir = clone(url=url)

    except Exception as e:
        print(e)
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return f"{dir} created."

if __name__ == "__main__":
    app.run(port=9900,debug=True)