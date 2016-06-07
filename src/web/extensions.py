from flask.ext.login import LoginManager
from flask_admin import Admin
from flask_mail import Mail

def create_login_manager():
    return LoginManager()

def create_admin():
    return Admin()

def create_mail():
    return Mail()

# flask-login
login_manager = create_login_manager()

# flask-admin
admin = create_admin()

# flask-mail
mail = create_mail()
