#!/usr/bin/env python
from flask import Flask, session, request, render_template, url_for, redirect
from config import config

app = Flask(__name__)


class Auth:
    def __init__(self):
        self.password = config.password
        self.users = config.users

    def login(self, user, password):
        if (password == self.password) and (user in self.users.keys()):
            return self.users[user]
        return False

    def isLoggedIn(self, user, token):
        return (user in self.users.keys()) and self.users[user] == token


@app.route('/')
def loginPage():
    return render_template('login.html', error=session.get('authError'))


@app.route('/login/', methods=['POST'])
def authenticate():
    try:
        password = request.form.get("password")
        username = request.form.get("username")
    except:
        return "something went wrong parsing the data."

    token = auth.login(username, password)
    if token:
        session['username'] = username
        session['token'] = token

        if 'authError' in session:
            del session['authError']

        return redirect(url_for("cam"))

    session['authError'] = "incorrect username or password"
    return redirect(url_for("loginPage"))


@app.route('/logout/', methods=['POST'])
def logout():
    del session['token']
    if 'authError' in session:
        del session['authError']

    return redirect(url_for("loginPage"))


@app.route("/cam")
def cam():
    if auth.isLoggedIn(session.get('username'), session.get('token')):
        return render_template('camera.html', stream=config.cameraURL)

    session['authError'] = 'missing or incorrect token'
    return redirect(url_for("loginPage"))


if __name__ == '__main__':
    auth = Auth()
    app.secret_key = config.secretKey

    # context = ('host.crt', 'host.key')
    # app.run(host='0.0.0.0', port='5000', ssl_context=context)
    
    app.run(host='0.0.0.0', port='5000')
