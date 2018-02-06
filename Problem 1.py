class Patient:
    """ base class """

    def __init__(self, name):
        """
        :param name: name of this patient
        """
        self.name = name

    def discharge(self):
        """
        abstract method to be overridden in derived classes
        :returns name and type of this patient
        """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class EmergencyPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)
        self.ecost = 1000 # not initialized in class so doesn't have to be inputted each time

    def discharge(self): # name is already remembered/inputted in the master class
        print(self.name, "Emergency Patient")


class HospitalizedPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)
        self.ecost = 2000

    def discharge(self):
        print(self.name, "Hospitalized Patient")

class Hospital:

    def __init__(self):
        """
        Think of it as like opening a brand new hospital with 0 cost and no patients.
        """
        self.patients = []
        self.cost = 0

    def admit(self, patients):
        self.patients.append(patients) #internally storing and adding to this internal storage at the same time


    def discharge_all(self):
        for patients in self.patients: #for each patient in the list of patients
            patients.discharge() #calling on discharge for self
            self.cost += patients.ecost


    def get_total_cost(self):
        return self.cost


# create patient nodes
Patient1 = EmergencyPatient('Patient 1')
Patient2 = EmergencyPatient('Patient 2')
Patient3 = EmergencyPatient('Patient 3')
Patient4 = HospitalizedPatient('Patient 4')
Patient5 = HospitalizedPatient('Patient 5')

YNHH = Hospital() #no attributes in hostpital therefore open brackets

YNHH.admit(Patient1) #admmitting patient 1 to YNHH
YNHH.admit(Patient2)
YNHH.admit(Patient3)
YNHH.admit(Patient4)
YNHH.admit(Patient5)

YNHH.discharge_all()

print(YNHH.get_total_cost())
