from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template("login.html", test="Testing")

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return "<p>Logout successful</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    return render_template("sign_up.html")