"""7-Crea una función llamada imprimir_pares que tome un número entero como
parámetro y imprima todos los números pares desde 1 hasta ese número."""

def imprimir_pares (a):
    for i in range (2,a+1,2):
        print (i)

a = int(input('Ingrese un número: '))

imprimir_pares (a)