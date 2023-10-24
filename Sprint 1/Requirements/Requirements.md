# Introduction
You've been asked by the newly formed Rutgers Health to create a patient-doctor appointment system. Create a system that categorizes illness into N categories and doctor medical specialization into M categories (where N > M). Ideally, every patient will get a doctor with the right speciality but that could result in long waiting times. You will need to make necessary assumptions of the number of patients, the number of doctors, acceptable waiting times (say based upon illness type) etc. but no patient must remain unseen for more than 14 days under any conditions.

# Requirements Engineering

## Assumptions (Brainstorm):

|||
|:----------------:|:----:|
|Database|Online and responsive|
|Appointment|Has to be made one day in advance|
|Condition|Patient can only request 1 condition for each appointment|
|Doctors|13 doctors available to treat patients|
|Patient|30 patients max seeking appointment times in the system. The patients will receive an appointment within 14 days of submission request|
|Specialities|There will be 13 specialities which doctors can acquire. Each of the 13 doctors are assigned to one of the specialities|
|Illnesses/Condition|Must be in the database|
|Patients Per Day Per Doctor|Max of 5 patients per day for each of the 13  available doctor|
|Location|Only 1 location for the Clinic|
|Duration of Appointment|Max of 1 hour long|
|Not included in System|No insurance eligibility check. Will not acquire patient medical history or past doctors. No appointment status/updates/notifications/reminders. No appointment confirmation. Patient cannot reschedule appointments (can only cancel). No patient check-in or check-out. No dashboard interface for employees. No emergency appointments available|

## Brainstorming

### Patient Portal

> Patient enters their condition in the portal. Then, the patient is given all available options for appointments based on their condition selection. If there is no doctor available (whether that is due to lack of appointment space or no doctor available pertaining to that specialty) for the patient’s selected condition, there will be no options listed on the portal. Additionally, the patient will have to make their appointment, if applicable 24 hours in advance. If any of these scenarios occur, the patient will then be redirected back to the home screen for the option to make a new appointment. Any appointments unscheduled by a patient or canceled appointments on the same day will not accept any fill-in slots. Once the patient selects the time and date, their name, illness, desired time/date will be logged in as data into the system. The patient will not receive any confirmation notifications through text or email.  

### Illness List

> Keep a list of acceptable illnesses and their respective urgency (or priority number). These acceptable illnesses will be determined by the 13 specialities in which the doctors acquire. 

### Appointments List

> List of appointments (doctor id, patient id, date/time of appointment) in order.