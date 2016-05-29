import bcrypt

from flask import render_template, request, redirect, url_for
from flask.ext.login import login_user
from wtforms import Form, TextField, PasswordField

from ...data.models import User
from ...data.db import db

def show():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if not form.password.data:
            return redirect(url_for('login.show'))

        user = db.session.query(User).filter_by(username=form.username.data).first()

        if not user:
            # user doesn't exist
            return redirect(url_for('login.show'))

        hashed_pw = bcrypt.hashpw(form.password.data.encode('utf-8'), user.salt.encode('utf-8'))

        if not user.password == hashed_pw:
            # passwords didn't match
            return redirect(url_for('login.show'))

        # flash a good thing
        login_user(user)
        return redirect(url_for('index.show'))

    return render_template('login/show.tmpl', form=form)

class LoginForm(Form):
    username = TextField('Username')
    password = PasswordField('Password')
