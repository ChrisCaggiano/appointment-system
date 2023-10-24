from flask import Flask, render_template, redirect, url_for, request, session
from database import *
from patient import *
from doctor import *
from categories import *
from appointment import *
from pprint import pprint
app = Flask(__name__)
app.secret_key =  b'_5#y2LsdfgQ8z\n\xec]/'

@app.route('/')
def hello_world():
  return "Hello world!"

@app.route('/home', methods=['GET', 'POST'])
def home():
  patient = get_patient(session.get('pid', 0))
  appointments = get_patient_appointments(patient.pid)
  if request.method == 'POST':
    return redirect(url_for('schedule'))
  return render_template('home.html', first_name=patient.first_name, appointments=appointments)

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
  patient = get_patient(session.get('pid', 0))
  options = get_potential_appointments(patient)
  pprint(options)
  if request.method == 'POST':
    [selected_did, selected_date_string] = request.form['apt_selected'].split('@')
    add_appointment(patient, get_doctor(selected_did), selected_date_string)
    return redirect(url_for('home'))
  return render_template('request.html', options=options, first_name=patient.first_name)

@app.route('/register', methods=['GET', 'POST'])
def register():
  illnesses = get_illnesses()
  if request.method == 'POST':
    print(request.form)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    illness = Illness[request.form['illness']]
    new_patient = Patient(first_name, last_name, illness)
    add_patient(new_patient)
    session['pid'] = new_patient.pid
    return redirect(url_for('home'))
  return render_template('register.html', illnesses=illnesses)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  print(request)
  if request.method == 'POST':
    print(request.form)
    if False:
      error = 'Invalid Credentials. Please try again.'
    else:
      session['pid'] = request.form['pid']
      return redirect(url_for('home'))
  return render_template('login.html', error=error)

if __name__ == '__main__':
  app.run()