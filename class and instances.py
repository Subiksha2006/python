class Hospital:
def __init__(self):
self.patients = {}

def add_patient(self, pid, name, age, disease):
self.patients[pid] = {
&quot;Name&quot;: name,
&quot;Age&quot;: age,
&quot;Disease&quot;: disease,
&quot;Doctor&quot;: &quot;Not Assigned&quot;,
&quot;Days&quot;: 0,
&quot;Bill&quot;: 0
}
return &quot;Patient Added Successfully&quot;

def assign_doctor(self, pid, doctor):
if pid in self.patients:
self.patients[pid][&quot;Doctor&quot;] = doctor
return &quot;Doctor Assigned&quot;
else:
return &quot;Patient ID Not Found&quot;

def generate_bill(self, pid, days, room_charge, medicine_charge):
if pid in self.patients:
bill = (days * room_charge) + medicine_charge
self.patients[pid][&quot;Days&quot;] = days
self.patients[pid][&quot;Bill&quot;] = bill
return bill
else:
return &quot;Patient ID Not Found&quot;

def display_patient(self, pid):
if pid in self.patients:
return self.patients[pid]
else:
return &quot;Patient ID Not Found&quot;

def discharge_patient(self, pid):
if pid in self.patients:
del self.patients[pid]
return &quot;Patient Discharged Successfully&quot;
else:
return &quot;Patient ID Not Found&quot;
