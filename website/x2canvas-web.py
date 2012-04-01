# encoding: UTF-8
import sys, os.path
import utils.whereami
from flask import Flask, request, session, g, redirect, url_for
from flask import abort, render_template, flash

USERNAME = 'admin'
PASSWORD = 'password'
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)



@app.route("/")
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_user'] = request.form['username'] 
    if 'logged_user' in session:
        flash('You were logged in')
        return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    if 'logged_user' in session:
        flash('You have been logged out')
        del session['logged_user']
    return redirect(url_for('login'))




if __name__ == "__main__":
    if '--debug' in sys.argv:
        app.debug = True
    app.run()
    
