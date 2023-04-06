from flask import Flask, render_template, request, jsonify

from chatAPI import get_response

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")