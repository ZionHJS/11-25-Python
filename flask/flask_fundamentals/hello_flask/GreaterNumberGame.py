import random 
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)

number = random.randint(1, 100)

@app.route('/', methods='POST')
def guess():
    curnum = request.form.inputNum
    info = ''
    if curnum > number:
        info = 'Too High'
    elif curnum < number:
        info = 'Too Low'
    else:
        info = '{{curnum}} is the number!'
    session['num'] = curnum
    return render_template('GreaterNumberGame.html', text=info)