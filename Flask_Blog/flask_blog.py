from flask import Flask, render_template,url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f2781dd262fa17b5b71f8d624b3c1da3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

posts = [
    {
        'author': 'Quoc Bao',
        'title': 'Blog Post 1',
        'content': 'Frist post content',
        'date_posted': 'April 20,2020'
    }, 
    {
        'author': 'Van Cong',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21,2020'
    }
]


@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title ='About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title = 'Register',form = form)

@app.route("/login",  methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): 
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been loggin in!!!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check username and password','danger')
    return render_template('login.html',title = 'Login',form = form)


if __name__ == '__main__':
    app.run(debug=True) 