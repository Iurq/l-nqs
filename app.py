from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def default_route():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/join')
def join():
    return render_template('join.html')

if __name__ == '__main__':
    app.run()
