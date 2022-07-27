from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sl_bd.db'
db = SQLAlchemy

@app.route("/")
def hello():
    return "<h2>hello world</h2>"


@app.route("/menu/<int:n>")
def proverka(n):
        if n == 1:
            return render_template('menu.html')
        if n == 2:
            return render_template('header.html')
        if n == 3:
            return render_template('menu.html')
        if n == 4:
            return render_template('header.html')
        if n == 5:
            return render_template('header.html')


@app.route('/menu')
def show_post():
    return render_template('menu.html')


if __name__ == "__main__":
    app.run()
