from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/profile')
def user_profile():
    return render_template('user-profile.html')