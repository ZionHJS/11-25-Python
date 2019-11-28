# This will be the "server" file where we will set up all of our routes to handle requests

from flask import Flask, render_template, request, redirect  # Import Flask class to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print('Got Post Info')
    print(request.form)   #request.form dictionary
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    return render_template('show.html', name_on_template=name_from_form, email_on_template=email_from_form)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.