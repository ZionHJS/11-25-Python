from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)
    name = request.form['name']
    email = request.from['email']
    return redirect('/show') #changed this line

#adding this method
@app.route('/show')
def show_user():
    print(request.form)
    return render_template('show.html')
