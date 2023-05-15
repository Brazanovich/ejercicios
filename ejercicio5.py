#5-Crea una función llamada es_divisible que tome dos números enteros como
#parámetros y devuelva Es divisible si el primer número es divisible por el
#segundo número, o No es divisible en caso contrario.

name = input("ingrese su nombre: ")
saludo = print(f" Bienvenido {name}. Continuamos con el ejercicio numero 5.")

def es_divisible(num1, num2):
    if num1 % num2 == 0 :
        print(f"{name}eL numero ingresado es divisible")
    else :
        print(f"{name} el numero ingresado no es divisible")

numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
es_divisible(numero1, numero2)
