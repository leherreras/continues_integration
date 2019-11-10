from flask import Flask, url_for, redirect
from flask_login import LoginManager

from apps.authentication.view import LoginView
from apps.diary.view import DiaryView

# Create the app with flask
app = Flask(__name__, template_folder="web/templates", static_folder="web/static")
app.secret_key = 'secret_api'
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Manage the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "LoginView:index"


@login_manager.user_loader
def load_user(user_id):
    return user_id  # TODO upload user


@app.route('/')
def home():
    return redirect(url_for('DiaryView:index'))


LoginView.register(app)
DiaryView.register(app)


if __name__ == '__main__':
    app.run(debug=True)
