from flask_app import app
from flask import render_template, redirect, request, session, flash
# from flask_app.models import model_login_reg

@app.route('/')
def index():
    if 'id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'id' not in session:
        return redirect('/')
    return render_template('dashboard.html')