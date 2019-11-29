from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('dojo_survey_index.html')

@app.route('/result', methods=['POST'])
def Submitted_Info():
    print(request.form)
    user_name = request.form['user_name']
    dojo_location = request.form['dojo_location']
    favorite_language = request.form['favorite_language']
    comment = request.form['comment']
    return render_template('dojo_survey_show.html', user_name=user_name, dojo_location=dojo_location, favorite_language=favorite_language, comment=comment)

if __name__=="__main__":   
    app.run(debug=True)   

