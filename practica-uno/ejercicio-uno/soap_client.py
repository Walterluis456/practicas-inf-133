from zeep import Client

client = Client('http://localhost:8000')

operacion = input("Ingrese la operacion que desea realizar (suma, resta, multiplicacion, division): ").lower()
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

if operacion == "suma":
    print(client.service.sumar(a, b))
elif operacion == "resta":
    print(client.service.restar(a, b))
elif operacion == "multiplicacion":
    print(client.service.multiplicar(a, b))
elif operacion == "division":
    print(client.service.dividir(a, b))
else:
    print("Operacion no valida")
