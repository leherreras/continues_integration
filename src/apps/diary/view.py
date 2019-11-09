import flask_login
from flask import render_template, request, url_for, flash, redirect
from flask_classy import FlaskView

from .controller import create_note


class LoginView(FlaskView):
    decorators = [flask_login.login_required]

    def index(self):
        return render_template('diary.html')

    def post(self):
        data = request.form.to_dict()
        message = create_note(data)
        flash(message)
        return redirect(url_for('LoginView:index'))
