from flask import Flask

from apps.authentication.view import LoginView
from apps.diary.view import DiaryView

app = Flask(__name__, template_folder="web/templates", static_folder="web/static")


@app.route('/')
def home():
    return "Hey there!"


LoginView.register(app)
DiaryView.register(app)


if __name__ == '__main__':
    app.run(debug=True)
