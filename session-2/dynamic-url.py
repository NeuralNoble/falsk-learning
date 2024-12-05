from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/welcome/<name>')
def welcome(name):
    return '<h1>Hello {}!</h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
