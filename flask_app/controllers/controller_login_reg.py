from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import model_login_reg

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/user/process_login', methods=['POST'])
def process_login():
    user = model_login_reg.User.get_one_email(email = request.form['user_input'])

    is_valid = True

    if not user:
        flash("Invalid Credentials", "user_input")
        is_valid = False

    if "password" in request.form and len(request.form['password']) < 1:
        flash("Must input a password", "pw")
        is_valid = False

    if user:
        if not bcrypt.check_password_hash(user.password, request.form['password']):
            is_valid = False
            flash('Invalid Credentials', "user_input")

    if not is_valid:
        return redirect('/')

    session['id'] = user.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.pop('id', None)
    return redirect('/')

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/user/create', methods=['POST'])
def create_user():
    is_valid = model_login_reg.User.validate_users(request.form)
    if not is_valid:
        return redirect('/')
    password = bcrypt.generate_password_hash(request.form['password'])

    data = {
        **request.form,
        'password': password
    }

    user_id = model_login_reg.User.create(data)
    session['id'] = user_id
    return redirect('/dashboard')



