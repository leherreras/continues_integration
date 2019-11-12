from flask import Flask, request, jsonify

from flask_sqlalchemy import SQLAlchemy

from marshmallow import Schema, fields

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50),nullable=False, unique=True)
    pwd = db.Column(db.String(50))

class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    pwd = fields.Str()

@app.route("/")
def index():

    return "Indice"

@app.route("/src/entities/")
def get_all_users():
    users = user.query.all()
    user_schema = UserSchema(many=True)
    results, errors = user_schema.dump(users)

    return jsonify(results)

@app.route("/src/entities/<string:name>", methods=["GET"])
def get_one_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    user_schema = UserSchema()
    result, errors = user_schema.dump(user)

    return jsonify(result)

@app.route("/src/entities/", methods=["POST"])
def add_user():
    new_user = User(email=request.json["email"],pwd=request.json["pwd"])
    db.session.add(new_user)
    db.session.commit()

    user_dict = {
            "id": new_user.id,
            "email": new_user.email
            "pwd": new_user.pwd
            }

    return jsonify(user_dict)

@app.route("/src/entities/<int:id>", methods=["PUT"])
def edit_user(id):
    user = User.query.filter_by(id=id).first()
    user.email = request.json["email"]
    user.pwd = request.json["pwd"]

    db.session.commit()

    user_dict = dict(id=user.id, name=user.email, pwd=user.pwd)

    return jsonify(user_dict)

@app.route("/src/entities/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = user.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "ok"})
