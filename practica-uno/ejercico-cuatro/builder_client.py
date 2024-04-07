import requests
import json

class PatientBuilder:
    def _init_(self):
        self.data = {}

    def with_ci(self, ci):
        self.data['ci'] = ci
        return self

    def with_name(self, name):
        self.data['name'] = name
        return self

    def with_age(self, age):
        self.data['age'] = age
        return self

    def with_gender(self, gender):
        self.data['gender'] = gender
        return self

    def with_diagnosis(self, diagnosis):
        self.data['diagnosis'] = diagnosis
        return self

    def with_doctor(self, doctor):
        self.data['doctor'] = doctor
        return self

    def send(self, url):
        headers = {'Content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(self.data), headers=headers)
        return response

if __name__ == "__main__":
    builder = PatientBuilder()
    response = builder.with_ci("1234567").with_name("Juanito").with_age(30).with_gender("Masculino").with_diagnosis("Diabetes").with_doctor("Pedro Pérez").send("http://localhost:8000/pacientes")
    print(response.text)