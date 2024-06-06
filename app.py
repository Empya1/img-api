from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bla.sqlite3"


db = SQLAlchemy(app)

class Bla(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	age = db.Column(db.Integer())
	time = db.Column(db.String())
	
with app.app_context():
	db.create_all()
	
@app.route("/")

def index():
	return jsonify({"hello":"yeah"})
	
@app.route("/saveimg",methods=["POST"])

def save_img():
	
	data = request.json
	
	return str(data)
