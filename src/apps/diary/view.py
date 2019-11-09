import flask_login
from flask import render_template, request, url_for, flash, redirect
from flask_classy import FlaskView
from flask_paginate import get_page_parameter, Pagination

from .controller import create_note, get_notes


class LoginView(FlaskView):
    decorators = [flask_login.login_required]

    def index(self):
        return render_template('diary.html')

    def post(self):
        data = request.form.to_dict()
        message = create_note(data)
        flash(message)
        return redirect(url_for('LoginView:index'))

    def notes(self):
        """
        use this library https://flask-paginate.readthedocs.io/en/latest/
        :return:
        """
        search = False
        q = request.args.get('q')
        if q:
            search = True
        page = request.args.get(get_page_parameter(), type=int, default=1)
        notes = get_notes(query=q)
        pagination = Pagination(page=page, total=notes.count(), search=search, record_name='notes')
        return render_template('notes.html', notes=notes, pagination=pagination)