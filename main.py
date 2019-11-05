from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    contex = {"results": "Hernando"}
    return render_template("index.html", **contex)


@app.route('/login')
def login():
    return "<h1>Login Here!</h1>"


if __name__ == '__main__':
    app.run(debug=True)
