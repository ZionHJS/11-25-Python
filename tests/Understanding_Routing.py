# This will be the "server" file where we will set up all of our routes to handle requests

from flask import Flask  # Import Flask class to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# '/' have it say "Hello World!"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# '/dojo' have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

# '/say/<name>' have it say Hi <name>
@app.route('/say/<name>')
def say(name):
    return "Hello" + name

# '/repeat/<num>/<name>' have it say "name" *num times
@app.route('/repeat/<num>/<name>')
def repeat(num, name):
    sum = name
    for x in range(0, num):
        sum = sum + name
    return sum
 
#change from paths
@app.route('/success')
def success():
  return "success"


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

