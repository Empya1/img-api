from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os




app = Flask(__name__)

app.config["SECRET_KEY"] = "SECRET KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bla.sqlite3"
app.config["UPLOAD_FOLDER"]= "uploads"
try: 
	os.mkdir(app.config["UPLOAD_FOLDER"])
	print("static created")
		
except:
	print("failef to create static")

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
	
	try:
		os.mkdir(app.config["UPLOAD_FOLDER"])
		
	except:
		print("failef to create static")
	
	data = request.json
	
	with open(f"""{app.config["UPLOAD_FOLDER"]}/a.jpg""", "wb") as p:
		t = data["image"]
		p.write(t.encode())
		p.close()
	
	return jsonify(data)

@app.route("/view")

def viewimg():
	print(os.path.join("a.jpg"))
		
	return render_template("img.html", url=str(f"""{app.config["UPLOAD_FOLDER"]}/a.jpg"""))
