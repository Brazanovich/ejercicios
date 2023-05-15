name = input("Escbribe tu nombre: ")
print(f" Aca vas a trabajar el ejercicio numero 1 de funciones {name}")

def suma(a, b):
    total = a + b
    return total 

a = int(input("Ingrese un numero: "))
b = int(input("ingrese un segundo numero: "))

resultado = suma(a, b)

print(f"La suma de {a} + {b} es {resultado}")