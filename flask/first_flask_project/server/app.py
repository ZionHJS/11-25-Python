from flask import Flask, render_template, redirect, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)