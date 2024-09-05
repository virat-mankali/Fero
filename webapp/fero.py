from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# MongoDB connection for login authentication
login_client = MongoClient('mongodb://localhost:27017/')
login_db = login_client['login_database']
users = login_db['users']

# MongoDB connection for bus stands
bus_client = MongoClient('mongodb://localhost:27017/')
bus_db = bus_client['bus_database']
bus_stands = bus_db['bus_stands']

# Check if the collection is empty before inserting bus stands
if bus_stands.count_documents({}) == 0:
    bus_stands.insert_many([
        {"name": "Pandit Nehru Bus Station", "location": "Vijayawada", "city": "Vijayawada"},
        {"name": "Dwaraka Bus Station", "location": "Visakhapatnam", "city": "Visakhapatnam"},
        {"name": "Tirupati Bus Stand", "location": "Tirupati", "city": "Tirupati"},
        {"name": "Itanagar Bus Stand", "location": "Itanagar", "city": "Itanagar"},
        {"name": "Pasighat Bus Stand", "location": "Pasighat", "city": "Pasighat"},
        {"name": "Tawang Bus Stand", "location": "Tawang", "city": "Tawang"},
        {"name": "ISBT Guwahati", "location": "Guwahati", "city": "Guwahati"},
        {"name": "Silchar Bus Stand", "location": "Silchar", "city": "Silchar"},
        {"name": "Dibrugarh Bus Stand", "location": "Dibrugarh", "city": "Dibrugarh"},
        {"name": "Bankipur Bus Stand", "location": "Patna", "city": "Patna"},
        {"name": "Muzaffarpur Bus Stand", "location": "Muzaffarpur", "city": "Muzaffarpur"},
        {"name": "Gaya Bus Stand", "location": "Gaya", "city": "Gaya"},
        {"name": "Pandri Bus Stand", "location": "Raipur", "city": "Raipur"},
        {"name": "Bilaspur Bus Stand", "location": "Bilaspur", "city": "Bilaspur"},
        {"name": "Durg Bus Stand", "location": "Durg", "city": "Durg"},
        {"name": "Panaji Bus Stand", "location": "Panaji", "city": "Panaji"},
        {"name": "Margao Bus Stand", "location": "Margao", "city": "Margao"},
        {"name": "Mapusa Bus Stand", "location": "Mapusa", "city": "Mapusa"},
        {"name": "Gita Mandir Bus Stand", "location": "Ahmedabad", "city": "Ahmedabad"},
        {"name": "Central Bus Station", "location": "Surat", "city": "Surat"},
        {"name": "Rajkot Bus Stand", "location": "Rajkot", "city": "Rajkot"},
        {"name": "ISBT Panchkula", "location": "Panchkula", "city": "Panchkula"},
        {"name": "Hisar Bus Stand", "location": "Hisar", "city": "Hisar"},
        {"name": "Rohtak Bus Stand", "location": "Rohtak", "city": "Rohtak"},
        {"name": "ISBT Tutikandi", "location": "Shimla", "city": "Shimla"},
        {"name": "Manali Bus Stand", "location": "Manali", "city": "Manali"},
        {"name": "Dharamshala Bus Stand", "location": "Dharamshala", "city": "Dharamshala"},
        {"name": "Khadgarha Bus Stand", "location": "Ranchi", "city": "Ranchi"},
        {"name": "Dhanbad Bus Stand", "location": "Dhanbad", "city": "Dhanbad"},
        {"name": "Jamshedpur Bus Stand", "location": "Jamshedpur", "city": "Jamshedpur"},
        {"name": "Majestic Bus Stand", "location": "Bengaluru", "city": "Bengaluru"},
        {"name": "Mysuru Bus Stand", "location": "Mysuru", "city": "Mysuru"},
        {"name": "Hubballi Bus Stand", "location": "Hubballi", "city": "Hubballi"},
        {"name": "Thiruvananthapuram Central Bus Station", "location": "Thiruvananthapuram", "city": "Thiruvananthapuram"},
        {"name": "Ernakulam KSRTC Bus Station", "location": "Kochi", "city": "Kochi"},
        {"name": "Kozhikode Bus Stand", "location": "Kozhikode", "city": "Kozhikode"},
        {"name": "Nadira Bus Stand", "location": "Bhopal", "city": "Bhopal"},
        {"name": "Sarwate Bus Stand", "location": "Indore", "city": "Indore"},
        {"name": "Gwalior Bus Stand", "location": "Gwalior", "city": "Gwalior"},
        {"name": "MSRTC Shivajinagar", "location": "Pune", "city": "Pune"},
        {"name": "Mumbai Central Bus Station", "location": "Mumbai", "city": "Mumbai"},
        {"name": "Nagpur Bus Stand", "location": "Nagpur", "city": "Nagpur"},
        {"name": "ISBT Imphal", "location": "Imphal", "city": "Imphal"},
        {"name": "Moirang Bus Stand", "location": "Moirang", "city": "Moirang"},
        {"name": "Kakching Bus Stand", "location": "Kakching", "city": "Kakching"},
        {"name": "Shillong Bus Stand", "location": "Shillong", "city": "Shillong"},
        {"name": "Tura Bus Stand", "location": "Tura", "city": "Tura"},
        {"name": "Jowai Bus Stand", "location": "Jowai", "city": "Jowai"},
        {"name": "Aizawl Bus Stand", "location": "Aizawl", "city": "Aizawl"},
        {"name": "Lunglei Bus Stand", "location": "Lunglei", "city": "Lunglei"},
        {"name": "Saiha Bus Stand", "location": "Saiha", "city": "Saiha"},
        {"name": "Dimapur Bus Stand", "location": "Dimapur", "city": "Dimapur"},
        {"name": "Kohima Bus Stand", "location": "Kohima", "city": "Kohima"},
        {"name": "Mokokchung Bus Stand", "location": "Mokokchung", "city": "Mokokchung"},
        {"name": "Baramunda Bus Stand", "location": "Bhubaneswar", "city": "Bhubaneswar"},
        {"name": "Badambadi Bus Stand", "location": "Cuttack", "city": "Cuttack"},
        {"name": "Berhampur Bus Stand", "location": "Berhampur", "city": "Berhampur"},
        {"name": "ISBT Mohali", "location": "Mohali", "city": "Mohali"},
        {"name": "Ludhiana Bus Stand", "location": "Ludhiana", "city": "Ludhiana"},
        {"name": "Amritsar Bus Stand", "location": "Amritsar", "city": "Amritsar"},
        {"name": "Sindhi Camp Bus Stand", "location": "Jaipur", "city": "Jaipur"},
        {"name": "Udaipur Bus Stand", "location": "Udaipur", "city": "Udaipur"},
        {"name": "Jodhpur Bus Stand", "location": "Jodhpur", "city": "Jodhpur"},
        {"name": "Gangtok Bus Stand", "location": "Gangtok", "city": "Gangtok"},
        {"name": "Singtam Bus Stand", "location": "Singtam", "city": "Singtam"},
        {"name": "Mangan Bus Stand", "location": "Mangan", "city": "Mangan"},
        {"name": "CMBT", "location": "Chennai", "city": "Chennai"},
        {"name": "Madhurai Integrated Bus Terminus", "location": "Madurai", "city": "Madurai"},
        {"name": "Salem Bus Stand", "location": "Salem", "city": "Salem"},
        {"name": "Mahatma Gandhi Bus Station", "location": "Hyderabad", "city": "Hyderabad"},
        {"name": "Jubilee Bus Station", "location": "Secunderabad", "city": "Secunderabad"},
        {"name": "Karimnagar Bus Stand", "location": "Karimnagar", "city": "Karimnagar"},
        {"name": "ISBT Tripura", "location": "Agartala", "city": "Agartala"},
        {"name": "Dharmanagar Bus Stand", "location": "Dharmanagar", "city": "Dharmanagar"},
        {"name": "Udaipur Bus Stand", "location": "Udaipur", "city": "Udaipur"},
        {"name": "Alambagh Bus Stand", "location": "Lucknow", "city": "Lucknow"}
    ])

# Registration form
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    signup = SubmitField('Sign Up')

# Login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    signin = SubmitField('Sign In')

@app.route('/', methods=['GET', 'POST'])
def login():
    reg_form = RegistrationForm()
    login_form = LoginForm()

    if request.method == 'POST':
        if 'signup' in request.form:
            if reg_form.validate_on_submit():
                name = reg_form.name.data
                email = reg_form.email.data
                password = reg_form.password.data
                if users.find_one({"email": email}):
                    flash("Email already registered", "danger")
                else:
                    hashed_password = generate_password_hash(password)
                    users.insert_one({"name": name, "email": email, "password": hashed_password})
                    flash("Registration successful", "success")
                    return redirect(url_for('login'))
        elif 'signin' in request.form:
            if login_form.validate_on_submit():
                email = login_form.email.data
                password = login_form.password.data
                user = users.find_one({"email": email})
                if user and check_password_hash(user['password'], password):
                    session['email'] = email
                    session['name'] = user['name']
                    flash("Login successful", "success")
                    return redirect(url_for('landing'))
                else:
                    flash("Invalid email or password", "danger")

    return render_template('loginpage.html', reg_form=reg_form, login_form=login_form)

@app.route('/fero')
def landing():
    if 'email' in session:
        name = session['name']
        return render_template('landingpage.html', name=name)
    else:
        flash("You need to login first", "danger")
        return redirect(url_for('login'))

@app.route('/choose_mode_of_transport')
def mode_of_transport():
    return render_template('modeoftransport.html')

@app.route('/buss_mode')
def buss_mode():
    return render_template('busmode.html')

@app.route('/landingpage')
def landing_page():
    return render_template('landingpage.html')

@app.route('/train_mode')
def train_mode():
    return render_template('trainmode.html')

@app.route('/metro_mode')
def metro_mode():
    return render_template('metromode.html')

@app.route('/metro_travel')
def metro_travel():
    return render_template('metrotravel.html')

@app.route('/buss_travel')
def bus_travel():
    bus_stands_list = list(bus_stands.find())
    return render_template('bustravel.html', bus_stands=bus_stands_list)

@app.route('/train_travel')
def train_travel():
    return render_template('traintravel.html')

@app.route('/customer_care')
def customer_care():
    return render_template('customercare.html')

@app.route('/about_us')
def about_us():
    return render_template('aboutus.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/terms_and_conditions')
def terms():
    return render_template('terms.html')

@app.route('/privacy_policy')
def privacypolicy():
    return render_template('privacypolicy.html')

if __name__ == '__main__':
    app.run(debug=True)
