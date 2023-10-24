from categories import Specialty, Illness, illness_match
from patient import Patient, inflate_patient
from appointment import Appointment
from doctor import Doctor, inflate_doctor
from pymongo import MongoClient
from datetime import date, datetime, timedelta
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.healthcare

# Return a list of Doctor - Date results
def get_potential_appointments(patient: Patient):
  specialty = illness_match(patient.illness)
  doctors = db.doctors
  result = []
  doctor_pointer = doctors.find({ "specialty": specialty })
  for doctor in doctor_pointer:
    doctor_obj = inflate_doctor(doctor)
    for day_delta in range(0, 14):
      new_date = date.today() + timedelta(days=day_delta)
      slots_left = doctor_obj.get_availability(new_date.__str__())
      information = str(doctor_obj.did) + "@" + new_date.__str__()
      if slots_left > 0:
        result.append((doctor_obj, new_date, information))
  return result

# Get a list of appointments on a give date
def get_appointments_on_date(date: date):
  db.appointments.find({"date": date.__str__()})
  pass

# Get the appointments for a given patient
def get_patient_appointments(pid):
  appointments = db.appointments.find({"pid": pid})
  output = []
  for appointment in appointments:
    output.append((get_doctor(appointment['did']), appointment['date'].__str__()))
  return output

# Assume that there is availability for said doctor
# Make sure it is not a duplicate
# Decrement the doctors slots on that day and add an appointment to the database
def add_appointment(patient: Patient, doctor: Doctor, date):
  if db.appointments.find_one({ 'pid': patient.pid, 'did': doctor.did, 'date': date.__str__()}):
    return False
  appointment = Appointment(patient=patient, doctor=doctor, date=date)
  doctor.schedule_appointment(date)
  db.appointments.insert_one(appointment.gen_object())
  db.doctors.update_one({ "did": doctor.did}, { "$set": { "schedule": doctor.schedule}})
  return True

# Add a doctor if they are not already registered in the system
def add_doctor(doctor: Doctor):
  if db.doctors.find_one({ "did": doctor.did}):
    return False
  db.doctors.insert_one(doctor.gen_object())
  return True

# Add a patient if they are not already registed in the system
def add_patient(patient: Patient):
  if db.patients.find_one({ "pid": patient.pid}):
    return False
  db.patients.insert_one(patient.gen_object())
  return True

# Get a doctor object based on the did 
def get_doctor(did):
  did = int(did)
  result = db.doctors.find_one({"did": did})
  if not result:
    return None
  return inflate_doctor(result)

# Get a patient object based on the pid
def get_patient(pid):
  pid = int(pid)
  result = db.patients.find_one({"pid": pid})
  if not result:
    return None
  return inflate_patient(result)