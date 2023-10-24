import random
class Patient:
  def __init__(self, first_name, last_name, illness, pid = 0):
    self.pid = pid
    self.first_name = first_name
    self.last_name = last_name
    self.illness = illness
    if self.pid == 0:
      self.pid = random.randint(1,9999)

  def gen_object(self):
    return {
      'pid': self.pid,
      'first_name': self.first_name,
      'last_name': self.last_name,
      'illness': self.illness.name,
    }

def inflate_patient(mongo_obj):
  pid = mongo_obj['pid']
  first_name = mongo_obj['first_name']
  last_name = mongo_obj['last_name']
  illness = mongo_obj['illness']
  return Patient(first_name, last_name, illness, pid)
