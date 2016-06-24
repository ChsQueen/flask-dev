from flask import render_template, jsonify, request, Response
from app import app


@app.route('/')
@app.route('/index')
def index():
   user = { 'nickname': 'Miguel' } # fake user
   array = [1,2,3,4]
   return render_template("index.html", title = 'Home', user = user, array=array)

@app.route('/email')
def email():
    return render_template("email.html")


@app.route("/stream")
def stream():
    def eventStream():
        for i in range(1, 100000):
            yield "{}. \n\n".format(i)
    return Response(eventStream(), mimetype="text/event-stream")