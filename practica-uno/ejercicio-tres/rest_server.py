# rest_server.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Lista de pacientes inicial
pacientes = [
    {
        "ci": "78496826",
        "nombre": "Juanito",
        "apellido": "Pérez",
        "edad": 30,
        "genero": "Masculino",
        "diagnostico": "Diabetes",
        "doctor": "Pedro Pérez"
    }
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/pacientes":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(pacientes).encode("utf-8"))
        elif self.path.startswith("/pacientes_ci"):
            ci = self.path.split("/")[-1]
            paciente = next(
                (p for p in pacientes if p["ci"] == ci),
                None
            )
            if paciente:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(paciente).encode("utf-8"))
            else:
                self.send_response(404)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"Error": "Paciente no encontrado"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    # Implementa el método do_POST para agregar pacientes, do_PUT para actualizar y do_DELETE para eliminar


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()