name = input("ingrese su nombre: ")
saludo = print(f" Bienvenido {name}. Continuamos con el ejercicio numero 3.")

#3-Crea una función llamada invertir_cadena que tome una cadena de texto como
#parámetro y devuelva la cadena invertida.

def invertir_cadena(cadena):
    return cadena [::-1]

text = input("Ingrese un texto: ")
resultado = invertir_cadena(text)
print(f" El texto invertido es {resultado}")