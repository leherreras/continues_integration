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
        redirect_next = request.args.get('next', url_for('DiaryView:index'))
        if authenticate(email, password):
            flash('Bienvenido a su diario', 'info')
        else:
            flash('Error de autenticacion', 'error')
        return redirect(redirect_next)


class LogoutView(FlaskView):
    decorators = [flask_login.login_required]

    @route('/', method=['POST', 'GET'])
    def logout(self):
        flask_login.logout_user()
        return redirect(url_for('LoginView:index'))
