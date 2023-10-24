from enum import Enum
class Specialty(Enum):
  IMMUNOLOGY = 1
  DERMATOLOGY = 2
  CARDIOLOGY = 3
  ENDOCRINOLOGY = 4
  GASTROENTEROLOGY = 5
  HEMATOLOGY = 6
  NEUROLOGY = 7
  ONCOLOGY = 9
  OTALARYNGOLOGY = 10
  PODIASTRIST = 11
  UROLOGY = 12
  PHYSICIAN = 13

class Illness(Enum):
  ASTHMA = 1
  ACNE = 2
  ANXIETY = 3
  DIABETES = 4
  EPILEPSY = 5
  ARTHRITIS = 6
  BRONCHITIS = 7
  IBS = 8
  FOOD_POISONING = 9
  GALLSTONES = 10
  WARTS = 11
  FEVER = 12
  LEUKAEMIA = 13
  MEASLES = 14
  MIGRAINE = 15
  PSORIASIS = 16
  SCOLIOSIS = 17
  COVID = 18

def illness_match(illness: Illness):
  if illness == Illness.COVID or illness == Illness.FEVER or illness == Illness.BRONCHITIS or illness == Illness.MEASLES:
    return Specialty.IMMUNOLOGY.name

  if illness == Illness.ACNE or illness == Illness.WARTS or illness == Illness.PSORIASIS:
    return Specialty.DERMATOLOGY.name
  
  if illness == Illness.MIGRAINE or illness == Illness.ANXIETY or illness == Illness.EPILEPSY or illness == Illness.SCOLIOSIS:
    return Specialty.NEUROLOGY.name
  
  if illness == Illness.GALLSTONES or illness == Illness.DIABETES:
    return Specialty.UROLOGY.name

  if illness == Illness.ARTHRITIS or illness == Illness.DIABETES:
    return Specialty.PODIASTRIST.name

  if illness == Illness.LEUKAEMIA:
    return Specialty.HEMATOLOGY.name

  if illness == Illness.FOOD_POISONING or illness == Illness.IBS:
    return Specialty.GASTROENTEROLOGY.name

  if illness == Illness.ASTHMA:
    return Specialty.OTALARYNGOLOGY.name

  return Specialty.PHYSICIAN.name

def get_illnesses():
  result = []
  for illness in Illness:
    result.append(illness.name)
  return result
  