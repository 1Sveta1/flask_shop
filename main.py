from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import flask_login
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sl_bd.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


@app.route("/category/<int:n>/")
def proverka(n):
    if 0 < n < 7:
        return render_template('category.html')


@app.route('/menu')
def show_post():
    return render_template('menu.html')


@app.route('/', methods=['POST', 'GET'])
def start():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        all_login = users.query.order_by(users.login).all()
        try:
            if login not in all_login():
                user = users(login=login, password=password)
                db.session.add(user)
                db.session.commit()
                return render_template("menu.html", data=all_login, pr=login)
        except:
            return render_template("category.html")
    else:
        return render_template('authorization.html')


if __name__ == "__main__":
    app.run()
