from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def counter():
    count = session['count']
    session['count'] = count + 1
    return render_template('index.html', counts=session['count'])

@app.route('/destory_session')
def clear():
    print('count exists!')
    session.clear()
    session['count'] = 0
    return redirect('/')