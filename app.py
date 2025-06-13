from flask import Flask,render_template,request

app = Flask(__name__,template_folder="templates",static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create",methods=["POST"])
def create():
    url = request.form.get("url")
    return url

if __name__ == "__main__":
    app.run(port=9900,debug=True)