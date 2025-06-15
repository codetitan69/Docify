from flask import Flask,render_template,request,abort
from http import HTTPStatus
from model import custom_request,api_key,Get_Content

from helpers import *

app = Flask(__name__,template_folder="templates",static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create",methods=["POST"])
def create():
    url = request.form.get("url")
    try:
        dir = clone(url=url)
        query = Create_Query("./"+dir+"/")
        response = custom_request(query,key=api_key)
        content = Get_Content(response)

    except Exception as e:
        print(e)
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)
    finally:
        pass 

    return f"{content}"

if __name__ == "__main__":
    app.run(port=9900,debug=True)