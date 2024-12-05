from flask import Flask , redirect , url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello World</h1>"

@app.route('/pass/<sname>/<int:marks>')
def passed(sname, marks):
    return f"<h1>congrats {sname.title()}Passed</h1>"

@app.route('/fail/<sname>/<int:marks>')
def failed(sname, marks):
    return f"<h1>congrats {sname.title()} failed</h1>"

@app.route('/score/<name>/<int:num>')
def scored(name,num):
    if num <30:
        return redirect(url_for('failed',sname=name,marks=num))
    else:
        return redirect(url_for('passed',sname=name,marks=num))


if __name__ == '__main__':
    app.run(debug=True)