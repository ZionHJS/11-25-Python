# This will be the "server" file where we will set up all of our routes to handle requests

from flask import Flask, render_template  # Import Flask class to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/lists')
def render_lists():
    student_info = [
        {'name':'Michael', 'age':35},
        {'name':'John','age':30},
        {'name':"Mark",'age':25},
        {'name':'Mark','age':27}
    ]
    return render_template("list.html", random_numbers=[3,1,5], students = students_info)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.