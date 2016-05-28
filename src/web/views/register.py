import bcrypt

from flask import render_template, request, redirect, url_for
from wtforms import Form, TextField, PasswordField, validators
from datetime import datetime

from ...data.models import User

def show():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(b'form.password.data', salt)
        user = User.create(
            username=form.username.data,
            password=hashed_pw,
            salt=salt,
            email=form.email.data,
            created_at=datetime.utcnow()
        )
        # flash a thing
        return redirect(url_for('index.show'))

    return render_template('register/show.tmpl', form=form)

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
