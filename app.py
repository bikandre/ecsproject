from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recruiters.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'

db = SQLAlchemy(app)
Bootstrap(app)

class Recruiter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        if not name or not email or not phone:
            flash("All fields are required!", "danger")
            return redirect('/')

        new_recruiter = Recruiter(name=name, email=email, phone=phone)
        db.session.add(new_recruiter)
        db.session.commit()
        flash("Contact details saved successfully!", "success")
        return redirect('/')

    recruiters = Recruiter.query.all()
    return render_template('index.html', recruiters=recruiters)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
