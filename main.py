from flask import Flask, render_template
from sqlalchemy import true

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


app.run(debug=True)