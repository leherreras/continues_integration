from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/notesdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(50), nullable = False, unique = True)
	pwd = db.Column(db.String(20))
	
	
	def __init__(self, email, pwd):
		self.email = email
		self.pwd = pwd
		
