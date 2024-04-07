# rest_client.py

import requests

url = "http://localhost:8000"
# GET consulta a la ruta /pacientes
ruta_get = f"{url}/pacientes"
get_response = requests.get(ruta_get)
print("Lista de todos los pacientes:")
print(get_response.json())

# GET consulta a la ruta /pacientes_ci/{ci}
ci_paciente = "78496826"
ruta_get_ci = f"{url}/pacientes_ci/{ci_paciente}"
get_ci_response = requests.get(ruta_get_ci)
print("\nPaciente con CI:", ci_paciente)
print(get_ci_response.json())