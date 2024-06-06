from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config["SECRET_KEY"] = "SECRET KEY"
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
	
	data = request.json()
	
	with open(os.path.join("a.jpg"), "wb") as p:
		p.write(data["image"])
	
	return jsonify(data)

@app.route("/view")

def viewimg():
	print(os.path.join("a.jpg"))
		
	return render_template("img.html", url=str(os.path.join("a.jpg")))

"""if __name__ == "__main__":	
	app.run()"""
