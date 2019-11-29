from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/users', methods=['POST'])
def create_user():
    print('Got Post Info')
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html') #session data is directly in our templates so we can use it without define variables
