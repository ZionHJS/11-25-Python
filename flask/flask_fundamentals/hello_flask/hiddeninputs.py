from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/process', methods=['POST'])
def which_form():
    if request.form['which_form'] == 'register':
    
    elif request.form['which_form'] == 'login':