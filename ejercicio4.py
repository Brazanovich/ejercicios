# 4-Crea una función llamada es_capicua que tome un número como parámetro y
# devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
# derecha a izquierda) y False en caso contrario.

def es_capicua(numero):
    numerosString = str(numero)
    if numerosString == numerosString[::-1]:
        print("Es Capicua")
    else:
        print ("No es Capicua")

numeroUser = input("Ingrese varios numeros para saber si es capicua: ")
es_capicua(numeroUser)