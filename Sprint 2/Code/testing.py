from doctor import Doctor
from patient import Patient
from categories import Specialty
from categories import Illness
from database import *
from datetime import date
from pprint import pprint

allen_doctor = Doctor("Allen", "Davis-Swing", Specialty.IMMUNOLOGY, 5,schedule={}, did=1234)
chris_patient = Patient("Chris", "Caggiano", Illness.COVID, 23423)

def test_make_doctor():
  assert Doctor("Allen", "Davis-Swing", Specialty.IMMUNOLOGY, 5,schedule={}, did=1234) != None

def test_register_doctor():
  assert add_doctor(allen_doctor)

def test_get_doctor():
  assert get_doctor(allen_doctor.did) != None

def test_make_patient():
  assert Patient("Chris", "Caggiano", Illness.COVID, 23423) != None

def test_register_patient():
  assert add_patient(chris_patient)

def test_get_patient():
  assert get_patient(chris_patient.pid) != None

def test_potential_appointments():
  assert get_potential_appointments(chris_patient) != None

def test_get_patient_appointments():
  assert get_patient_appointments(chris_patient.pid) != None