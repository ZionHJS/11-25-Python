from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)

@app.route('/')
def counter():
    count = session['count']
    session['count'] = int(count) + 1
    return render_template('counter.html', counts=session['count'])

@app.route('/destory_session')
def clear():
    if 'count' in session:
        print('count exists!')
    else:
        print('count does NOT exist')
    session.clear()
    session['count'] = 0
    return redirect('/')