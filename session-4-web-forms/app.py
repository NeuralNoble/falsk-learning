from flask import Flask, render_template , request, redirect, url_for,flash
from  forms import SignupForm , LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this_is_secret_key'

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",title="Home")

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data
    if form.validate_on_submit():
        flash('Login Successful')
        return redirect(url_for('home'))
    return render_template("login.html",title="Login",form=form)

@app.route('/signup',methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'You are now registered {form.username.data}')
        return redirect(url_for('home'))
    return render_template("signup.html",title="Signup",form=form)

if __name__ == '__main__':
    app.run(debug=True)

