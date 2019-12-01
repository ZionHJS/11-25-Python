from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('pet_flask')
    pets = mysql.query_db('SELECT * FROM pets')
    return render_template('C+R_pets.html', all_pets=pets)

@app.route('/addpet', methods=['POST'])
def add_pet_to_db():
    mysql = connectToMySQL('pet_flask')
    query = 'INSERT INTO pets(name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW())'
    data = {
        'name':request.form['name'],
        'type':request.form['type']
    }
    new_pet_id = mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
