from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Hello World</h1>"

@app.route('/about')
def about():
    return "<h1>About</h1>"

@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1>Hello {name.title()}</h1>"

@app.route('/addition/<int:a>/<int:b>')
def addition(a,b):
    return f"{a+b}"

if __name__ == '__main__':
    app.run(debug=True)
