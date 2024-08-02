from app import app, db
from flask import render_template, request, redirect, url_for

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/teacher_dashboard')
def teacher_dashboard():
    return render_template('teacher_dashboard.html')

@app.route('/student_dashboard')
def student_dashboard():
    return render_template('student_dashboard.html')

@app.route('/my_class')
def my_class():
    return render_template('my_class.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Implement login logic
    return redirect(url_for('admin_dashboard'))
