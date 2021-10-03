from flask import Flask, redirect, url_for, render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def show_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()