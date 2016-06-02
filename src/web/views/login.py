import bcrypt
import hmac
import urllib
import json

from flask import render_template, request, redirect, url_for
from flask.ext.login import login_user, logout_user
from wtforms import Form, TextField, PasswordField, HiddenField

from ...data.models import User
from ...data.db import db
from ...settings import app_config

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

def forgot_password():
    if request.method == 'GET':
        return """
            <p>Forget your password? Enter your email below to reset it.</p>
            <form method='POST'>
                <input type='text' name='reset_email' />
                <button type='submit'>Reset your password</button>
            </form>"""
    else:
        payload = create_payload(request.form['reset_email'])
        url = "/reset_password?%s" % get_url_keys(payload)
        return """
            <p>
                This will be an email.
            </p>
            <a href="%(url)s">
                %(url)s
            </a>""" % {"url": url}

def reset_password():
    email = request.args.get('email')
    auth_code = request.args.get('auth_code')
    form = PasswordResetForm(request.form, email=email, auth_code=auth_code)
    if request.method == 'GET':
        try:
            payload = {"email": str(email)}
            auth_code = str(auth_code)
            check_password_reset(payload, auth_code)
        except PasswordResetError:
            return redirect(url_for('index.show'))

        return render_template('login/reset_password.tmpl', form=form)
    elif request.method == 'POST':
        email = form.email.data
        auth_code = form.auth_code.data
        if not form.password.data == form.confirm.data:
            return redirect(url_for('login.reset_password', email=email, auth_code=auth_code))

        user = db.session.query(User).filter_by(email=email).first()
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(form.password.data.encode('utf-8'), salt)

        user.update(password=hashed_pw, salt=salt)
        return redirect(url_for('login.show'))


def logout():
    logout_user()
    return redirect(url_for('index.show'))

def get_auth_code(payload):
    return hmac.new(str(app_config.SECRET_KEY), json.dumps(payload)).hexdigest()

def create_payload(email):
    return {"email": str(email)}

def get_url_keys(payload):
    url_keys = {'auth_code': get_auth_code(payload)}
    url_keys.update(payload)
    return urllib.urlencode(url_keys)

def check_password_reset(payload, auth_code):
    new_code = get_auth_code(payload)
    if new_code != auth_code:
        raise PasswordResetError("Codes did not match")

class LoginForm(Form):
    username = TextField('Username')
    password = PasswordField('Password')

class PasswordResetForm(Form):
    password = PasswordField('Password')
    confirm = PasswordField('Confirm')
    email = HiddenField('')
    auth_code = HiddenField('')

class PasswordResetError(Exception):
    pass
