from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login successful</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout successful</p>"

@auth.route('/sign-up')
def signup():
    return "<p>Sign up</p>"