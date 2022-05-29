from flask import  Flask, request

app = Flask("something")

@app.route("/name",methods=["GET","POST","DELETE"])
def hello():
    if request.method=="GET":
        # a = 1/0
        return '<h1><div id="moshe"><li>mazda</li>"'
    if requests.method=="POST":
        return "save new car"

app.run(host="0.0.0.0",port=5001)