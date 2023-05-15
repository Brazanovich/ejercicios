# 6-Crea una función llamada es_par que tome un número como parámetro y
# devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
# devuelva Es impar o No es par.

name = input("ingrese su nombre: ")
saludo = print(f" Bienvenido {name}. Continuamos con el ejercicio numero 6.")



def esPar(numero):
    if numero % 2 == 0:
        print(f"{name} el numero que ingreso es PAR")
    else:
        print(f"{name} el numero que ingreso NO ES PAR")


numeroUser = int(input("Ingrese un numero para saber si es PAR: "))
esPar(numeroUser)