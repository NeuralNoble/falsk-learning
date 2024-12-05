from flask import Flask ,redirect,url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World!'


@app.route('/welcome/<name>')
def welcome(name):
    return '<h1>Hello {}!</h1>'.format(name)

@app.route('/pass')
def passed():
    return  f'<h1>You have passed!</h1>'

@app.route('/fail')
def failed():
    return f'<h1>You have failed!</h1>'


@app.route('/score/<name>/<int:num>')
def score(name, num):
    if num < 30:
        return redirect(url_for('failed'))
    else:
        return redirect(url_for('passed'))



if __name__ == '__main__':
    app.run(debug=True)
