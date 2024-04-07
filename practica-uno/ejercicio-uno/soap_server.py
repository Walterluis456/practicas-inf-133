from http.server import HTTPServer, BaseHTTPRequestHandler
from pysimplesoap.server import SoapDispatcher, SOAPHandler

# Definir las operaciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

dispatcher = SoapDispatcher(
    "ejercicio-uno",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns="http://localhost:8000"
)

dispatcher.register_function(
    "sumar",
    sumar,
    returns={"result": int},
    args={"a": int, "b": int}
)

dispatcher.register_function(
    "restar",
    restar,
    returns={"result": int},
    args={"a": int, "b": int}
)

dispatcher.register_function(
    "multiplicar",
    multiplicar,
    returns={"result": int},
    args={"a": int, "b": int}
)

dispatcher.register_function(
    "dividir",
    dividir,
    returns={"result": float},
    args={"a": int, "b": int}
)

# Iniciar el servidor
try:
    server = HTTPServer(("localhost", 8000), SOAPHandler)
    server.dispatcher = dispatcher
    print("Server started")
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
    print("Server stopped")
