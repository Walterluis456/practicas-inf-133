from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Patient:
    def _init_(self, ci, name, age, gender, diagnosis, doctor):
        self.ci = ci
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.doctor = doctor

    def to_json(self):
        return {
            "ci": self.ci,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "diagnosis": self.diagnosis,
            "doctor": self.doctor
        }

class PatientResponseBuilder:
    @staticmethod
    def build_success_response(data):
        response = {
            "status": "success",
            "data": data.to_json()
        }
        return json.dumps(response).encode("utf-8")

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))

        patient = Patient(post_data['ci'], post_data['name'], post_data['age'], post_data['gender'], post_data['diagnosis'], post_data['doctor'])

        self.send_response(201)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(PatientResponseBuilder.build_success_response(patient))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando servidor web en http://localhost:{port}/")
    httpd.serve_forever()

if __name__ == "__main__":
    run()