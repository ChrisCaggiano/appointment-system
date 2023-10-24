from categories import Specialty
from datetime import date
import random

class Doctor:
  def __init__(self, first_name, last_name, specialty: Specialty, patient_slots, schedule={}, did = 0):
    self.did = did
    self.first_name = first_name
    self.last_name = last_name
    self.specialty = specialty
    self.patient_slots = patient_slots
    self.schedule = schedule
    if self.did == 0:
      self.did = random.randint(1,9999)

  def get_availability(self, date):
    if date.__str__() in self.schedule:
      return self.schedule[date.__str__()]
    else:
      self.schedule[date.__str__()] = self.patient_slots
      return self.patient_slots

  def schedule_appointment(self, date):
    if self.get_availability(date) > 0:
      self.schedule[date.__str__()] = self.schedule[date.__str__()] - 1
      return True
    else: 
      return False

  def gen_object(self):
    doctor_object = {
      'did': self.did,
      'first_name': self.first_name,
      'last_name': self.last_name,
      'specialty': self.specialty.name,
      'patient_slots': self.patient_slots,
      'schedule': self.schedule
    }
    return doctor_object

def inflate_doctor(mongo_obj):
  did = mongo_obj['did']
  first_name = mongo_obj['first_name']
  last_name = mongo_obj['last_name']
  patient_slots = mongo_obj['patient_slots']
  schedule = mongo_obj['schedule']
  specialty = mongo_obj['specialty']
  return Doctor(first_name, last_name, specialty, patient_slots, schedule, did)