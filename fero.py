from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

client = MongoClient('mongodb://localhost:27017/')
db = client['login_system']
users = db['users']

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

@app.route('/', methods=['GET', 'POST'])
def index():
    reg_form = RegistrationForm()
    login_form = LoginForm()
    if request.method == 'POST':
        if 'signup' in request.form and reg_form.validate():
            existing_user = users.find_one({'email': reg_form.email.data})
            if existing_user is None:
                hashpass = bcrypt.hashpw(reg_form.password.data.encode('utf-8'), bcrypt.gensalt())
                users.insert_one({'name': reg_form.name.data, 'email': reg_form.email.data, 'password': hashpass})
                flash('Registration Successful!', 'success')
            else:
                flash('Email already exists!', 'danger')
            return redirect(url_for('index'))

        elif 'signin' in request.form and login_form.validate():
            user = users.find_one({'email': login_form.email.data})
            if user and bcrypt.checkpw(login_form.password.data.encode('utf-8'), user['password']):
                flash('Login Successful!', 'success')
            else:
                flash('Invalid email or password', 'danger')
            return redirect(url_for('index'))

    return render_template('loginpage.html', reg_form=reg_form, login_form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
