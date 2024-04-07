import requests

url = 'http://localhost:8000/graphql'

query_lista ="""
{
    plantas{
        id
        nombre
        especie
        edad
        altura
        fruto
    }
}"""
response = requests.post(url, json={'query': query_lista})
print(response.text)

query_crear ="""
    mutation {
        crearPlanta(
            nombre: "Secuoya",
            especie: "Sequoia sempervirens",
            edad: 42,
            altura: 240,
            fruto: true
        ) {
            planta {
                id
                nombre
                especie
                edad
                altura
                fruto
            }
        }
    }
"""
response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

query_especie ="""
{
    buscarEspecie(especie: "Pinus") {
        id
        nombre
        especie
        edad
        altura
        fruto
    }
}
"""
response = requests.post(url, json={'query': query_especie})
print(response.text)

query_editar ="""
    mutation {
        editarPlanta(
            id: 2,
            nombre: "Manzano",
            especie: "Malus domestica",
            edad: 36,
            altura: 150,
            fruto: true
        ) {
            planta {
                id
                nombre
                especie
                edad
                altura
                fruto
            }
        }
    }
"""
response = requests.post(url, json={'query': query_editar})
print(response.text)

query_frutos="""
    {
        frutos{
                id
                nombre
                especie
                edad
                altura
                fruto
            }
    }
"""
response = requests.post(url, json={'query': query_frutos})
print(response.text)

query_eliminar ="""
    mutation {
        eliminarPlanta(id: 1) {
            planta {
                id
                nombre
                especie
                edad
                altura
                fruto
            }
        }
    }
"""
response = requests.post(url, json={'query': query_eliminar})
print(response.text)
