from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/process', methods=['POST'])
def which_form():
    