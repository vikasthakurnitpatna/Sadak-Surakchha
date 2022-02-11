from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/jaankari"
db = SQLAlchemy(app)


class Complaint(db.Model):
    name = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(12), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    pincode = db.Column(db.String(15), nullable=False)
    sno = db.Column(db.Integer, primary_key=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/query", methods=['GET', 'POST'])
def query():
    if(request.method == 'POST'):
        name = request.form.get('name')
        city = request.form.get('city')
        state = request.form.get('state')
        pincode = request.form.get('pincode')
        entry = Complaint(name=name, city=city, state=state, pincode=pincode)
        db.session.add(entry)
        db.session.commit()

    return render_template("query.html")


app.run(debug=True)
