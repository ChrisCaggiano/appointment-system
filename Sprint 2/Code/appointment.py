from datetime import date
from doctor import Doctor 
from patient import Patient
from datetime import date
class Appointment:
  def __init__(self, date, doctor: Doctor, patient: Patient):
    self.date = date
    self.did = doctor.did
    self.pid = patient.pid
    self.information = str(doctor.did) + " " + date.__str__()
  
  def gen_object(self):
    return {
      'did': self.did,
      'pid': self.pid,
      'date': self.date.__str__()
    }