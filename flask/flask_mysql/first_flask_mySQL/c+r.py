from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('pet_flask')
    pets = mysql.query_db('SELECT * FROM pets')
    return render_template('C+R_pets.html', all_pets=pets)

@app.route()