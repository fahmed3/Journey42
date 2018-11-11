from flask import Flask, render_template, request, redirect, url_for, session, flash, Response
from utils import auth, database
import os, json

app = Flask(__name__)

def make_secret_key():
    return os.urandom(32)

app.secret_key = make_secret_key()

app.jinja_env.globals.update(logged_in = auth.logged_in)

#index: Home page. Renders index.html
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        #is this a valid username?
        if auth.user_exists(username):
            if auth.login(username, password):
                return redirect('index')
            else:
                flash('Login Error: You have entered the wrong password.')
        else:
            flash('Login Error: This username does not exist in the database. Check for any spelling errors or register a new account!')
    return render_template('login.html')


#logout: Logs the user out of the session. Redirects to index after logging out.
@app.route('/logout')
def logout():
    if auth.logged_in():
        auth.logout()
        flash('You have been logged out.')
    else:
        flash('Logout Error: You are not logged in.')
    return redirect('index')

@app.route('/profile')
def profile():
    if auth.logged_in():
        name = session['username']
        return render_template('profile.html', name=name) #likes, places
    else:
        flash('Access error. You are not logged in.')
        return redirect('index')        

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if auth.new_user(username, password):
            flash('Account successfully created! Log in with your new account.')
            return redirect('login')
        else:
            flash('Registration error: Username is already in use.')
    return render_template('register.html')

@app.route('/find_friends', methods=['GET', 'POST'])
def find_friends():
    if auth.logged_in():
        if request.method == 'POST':
            #place = request.form.get('search_places')
            #users = database.get_users(place)
            users = ['Lisa', 'Christina'] #hardcoded in, database doesn't exist
            return render_template('find_friends.html',
                                   users = users)
    else:
        flash('Access error. You are not logged in.')
        return redirect('index')            

@app.route('/search.js')
def jsfile():
    json_data = open('data.json').read()
    data = json.loads(json_data)
    return Response(render_template("search.js",
                                     data = json.dumps(data) ),
                        mimetype="text/javascript")

if __name__ == '__main__':
    app.debug = True
    app.run()

