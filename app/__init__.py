import datetime
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    if len(text) > 0:
        print(f"{datetime.datetime.now()} {text}")
        return render_template("yo_page.html", nickname=text)
    else:
        return render_template("index.html")
