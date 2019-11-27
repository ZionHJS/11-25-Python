# This will be the "server" file where we will set up all of our routes to handle requests

from flask import Flask, render_template  # Import Flask class to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html", phrase="hello", times=5)   #notice the 2 new arguments

# route for play
@app.route('/play')
def play1():
    return render_template('play.html')
@app.route('/play/<x>')
def play2(x):
    return render_template('play.html', times=int(x))
@app.route('/play/<x>/<color>')
def play3(x, color):
    return render_template('play.html', times=int(x), color=color)

#change from paths
@app.route('/success')
def success():
    return "success"

#variable rules
@app.route('/hello/<name>')
def hello(name):
    return "Hello, " + name

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id" + id

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

