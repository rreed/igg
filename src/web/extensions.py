import os
import json
import paypalrestsdk

from flask.ext.login import LoginManager
from flask_admin import Admin
from flask_mail import Mail

def create_login_manager():
    return LoginManager()

def create_admin():
    return Admin()

def create_mail():
    return Mail()

def create_paypal():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    try: # dev
        with open(os.path.join(__location__, 'secrets.json')) as secrets_file:
            secrets = json.load(secrets_file)

            paypalrestsdk.configure({
                "mode": "sandbox", # sandbox or live
                "client_id": secrets.get('paypal_id'),
                "client_secret": secrets.get('paypal_secret')
            })

            return paypalrestsdk
    except IOError: # prod
        paypalrestsdk.configure({
            "mode": "sandbox", # sandbox or live
            "client_id": os.environ.get("PAYPAL_ID"),
            "client_secret": os.environ.get("PAYPAL_SECRET")
        })

# flask-login
login_manager = create_login_manager()

# flask-admin
admin = create_admin()

# flask-mail
mail = create_mail()

# paypalrestsdk
paypal = create_paypal()
