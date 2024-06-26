from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from graphene import ObjectType, Int, String, Boolean, List, Schema, Field, Mutation

class Planta(ObjectType):
    id = Int() 
    nombre = String() 
    especie = String() 
    edad =  Int()  
    altura = Int() 
    fruto = Boolean()

class Query(ObjectType):
    plantas = List(Planta)
    buscar_especie = Field(List(Planta), especie=String())
    frutos = Field(List(Planta))

    def resolve_plantas(self, info):
        return [Planta(
            id=1,
            nombre='Pino',
            especie='Pinus',
            edad=24,
            altura=120,
            fruto=False
        ), Planta(
            id=2,
            nombre='Manzano',
            especie='Malus domestica',
            edad=36,
            altura=150,
            fruto=True
        )]
    
    def resolve_buscar_especie(self, info, especie):
        if especie == 'Pinus':
            return [Planta(
                id=1,
                nombre='Pino',
                especie='Pinus',
                edad=24,
                altura=120,
                fruto=False
            )]
        else:
            return []
    
    def resolve_frutos(self, info):
        return [Planta(
            id=2,
            nombre='Manzano',
            especie='Malus domestica',
            edad=36,
            altura=150,
            fruto=True
        )]

class CrearPlanta(Mutation):
    class Arguments:
        nombre = String()
        especie = String()
        edad = Int()
        altura = Int()
        fruto = Boolean()
    
    planta = Field(Planta)
    
    def mutate(self, info, nombre, especie, edad, altura, fruto):
        return CrearPlanta(planta=Planta(
            id=3,
            nombre=nombre,
            especie=especie,
            edad=edad,
            altura=altura,
            fruto=fruto
        ))

class EditarPlanta(Mutation):
    class Arguments:
        id = Int()
        nombre = String()
        especie = String()
        edad = Int()
        altura = Int()
        fruto = Boolean()
    
    planta = Field(Planta)
    
    def mutate(self, info, id, nombre, especie, edad, altura, fruto):
        return EditarPlanta(planta=Planta(
            id=id,
            nombre=nombre,
            especie=especie,
            edad=edad,
            altura=altura,
            fruto=fruto
        ))

class EliminarPlanta(Mutation):
    class Arguments:
        id = Int()
    
    planta = Field(Planta)
    
    def mutate(self, info, id):
        return EliminarPlanta(planta=Planta(
            id=id,
            nombre='Cerezos',
            especie='Prunus',
            edad=24,
            altura=120,
            fruto=False
        ))

class Mutations(ObjectType):
    crear_planta = CrearPlanta.Field()
    editar_planta = EditarPlanta.Field()
    eliminar_planta = EliminarPlanta.Field()

schema = Schema(query=Query, mutation=Mutations)

class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()
