from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from PIL import Image
from io import BytesIO



app = Flask(__name__)

app.config["SECRET_KEY"] = "SECRET KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bla.sqlite3"
app.config["UPLOAD_FOLDER"]= "uploads"
try: 
	os.mkdir(app.config["UPLOAD_FOLDER"])
	print("static created")
		
except:
	print("failef to create upload folder")

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
		print("failef to create upload folder")
	
	data = request.files["image"]
	print(data)
	
	data.save(os.path.join(app.config["UPLOAD_FOLDER"], "a.jpg"))
	
	#image = Image.open(BytesIo(data["image"]))
	#image.save(f"""{app.config["UPLOAD_FOLDER"]}/b.jpg""")
	
	return jsonify({"oh yeah":"were fone"})

@app.route("/view")

def viewimg():
	print(os.path.join("a.jpg"))
		
	return render_template("img.html", url=str(os.path.join(app.config["UPLOAD_FOLDER"], "a.jpg")))
