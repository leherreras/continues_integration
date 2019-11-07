import flask_login
from flask import render_template, request, url_for, flash, redirect
from flask_classy import FlaskView, route

from .controller import authenticate


class LoginView(FlaskView):

    def index(self):
        return render_template('login.html')

    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')
        if authenticate(email, password):
            redirect_next = request.args.get('next', url_for('DiaryView:index'))
            flash('Bienvenido a su diario', 'info')
            return redirect(redirect_next)


class LogoutView(FlaskView):
    decorators = [flask_login.current_user]

    @route('/', method=['POST', 'GET'])
    def logout(self):
        flask_login.logout_user()
        return redirect(url_for('LoginView:index'))
