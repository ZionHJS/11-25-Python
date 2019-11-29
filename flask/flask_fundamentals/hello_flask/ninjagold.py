from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/process_money')
def gold():
    if request.form['building'] == 'farm':
        
    elif request.form['building'] == 'cave':
    
    elif request.form['building'] == 'house'

    elif request.form['building'] == 'casino'

@app.route('/')
def show():
    return render_template('')