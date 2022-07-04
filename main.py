from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h2>hello world</h2>"


@app.route('/menu')
def show_post():
    return render_template('menu.html')


if __name__ == "__main__":
    app.run()
