from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

#The two strange @app.route lines above the function are decorators a unique feature of the Python language. 
#A decorator modifies the function that follows it. 

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fatih'}
    posts = [
        {
            'author': {'username': 'Yavuz'},
            'body': 'Im too busy working on Speech and Debate!'
        },
        {
            'author': {'username': 'Beyza'},
            'body': 'iPad istiyorum!'

        }
    ]
    #The operation that converts a template into a complete HTML page is called rendering
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
