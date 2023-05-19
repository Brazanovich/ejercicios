# lista de nombres :
# Mauricio Iván Stalcar
# Ebrain Ramirez Figueroa
# Valeria Margarita Nuñez
# Elias Alejandro Brazanovich
# Rodríguez, Exequiel Agustín
# Arrejin, Nicolas Miguel
# Braian Maximiliano Diaz Juarez
# Mario Rodriguez

def menu():
        print("MENU DE INMUEBLES")
        print("1. Agregar propiedad")
        print("2. Editar propiedad")
        print("3. Eliminar propiedad")
        print("4. Editar estado")
        print("5. Ver lista")
        print("6. Lista de precios")
        print("7. Salir")

#AÑADIR PROPIEDAD
def añadir_propiedad(propiedades):
    año = int(input("Año: "))
    metros = int(input("Metros cuadrados: "))
    habitaciones = int(input("Número de habitaciones: "))
    garage = True if input("Garaje (S/N): ").upper() == "S" else False
    zona = input("Zona (A/B/C): ").upper()
    if zona not in ["A", "B", "C"]:
        print("La zona ingresada no es válida.")
        return
    if año < 2000:
        print("El inmueble debe ser del año 2000 o posterior.")
        return
    if metros < 60:
        print("El inmueble debe tener al menos 60 metros cuadrados.")
        return
    if habitaciones < 2:
        print("El inmueble debe tener al menos 2 habitaciones.")
        return
    nueva_propiedad = {
        "año": año,
        "metros": metros,
        "habitaciones": habitaciones,
        "garaje": garage,
        "zona": zona,
        "estado": "Disponible"
    }
    propiedades.append(nueva_propiedad)
    print("Inmueble agregado exitosamente.")

#ELIMINAR PROPIEDAD
def eliminar_propiedad(propiedades):
    eliminar = int(input("Elija el Indice de inmueble a eliminar:"))
    try:
        print("Seguro quieres eliminar: ")
        print(f"{propiedades[eliminar]}?")
        confirm = input("Para confirmar ustilice SI: ")
        if confirm == "SI" or confirm == "si":
            del propiedades[eliminar]
            print("Inmueble eliminado correctamente")
        else:
            print('Cancelando...')
    except IndexError:
        print("Ese valor no existe.")
        input("Presione enter para continuar")
#EDITAR LA PROPIEDAD
def editar_propiedad():
    index = int(input("Elija el numero con el indice a editar: "))
    if index >= 0 and index < len(propiedades):
        print(f"Vas a editar \n{propiedades[index]}")
        añoedit = int(input("Ingrese el año: "))
        metrosedit = int(input("Ingrese los metros: "))
        habitacionesedit = int(input("Ingrese las cantidad de habitaciones: "))
        garajedit = True if input("Garaje (S/N): ").upper() == "S" else False
        zonaedit = input("Ingrese la zona: ").upper()
        estadoedit = input("Ingrese el estado: ")
        InmuebleNuevo = {}
        InmuebleNuevo['año'] = añoedit
        InmuebleNuevo['metros'] = metrosedit
        InmuebleNuevo['habitaciones'] = habitacionesedit
        InmuebleNuevo['garaje'] = garajedit
        InmuebleNuevo['zona'] = zonaedit
        InmuebleNuevo['estado'] = estadoedit
#ACTUALIZA EL INMUEBLE EN LA LISTA CON LOS NUEVOS DATOS .UPDATE()
        propiedades[index].update(InmuebleNuevo)
        print("Se a editado con exito.")

#CAMBIAR EL ESTADO DEL INMUEBLE
def modificar_estado():
    index = int(input("Elija el numero con el indice a editar: "))
    if index >= 0 and index < len(propiedades):
        print(f"Vas a editar \n{propiedades[index]['estado']}")
        estadoedit = input("Ingrese el estado: ")
        InmuebleNuevo = {}
        InmuebleNuevo['estado'] = estadoedit
        propiedades[index].update(InmuebleNuevo)
        print("Se a editado con exito.")

#VER LISTA
def ver_lista():
    for index, value in enumerate(propiedades):
        print("Indice: ", index, "Value: ", value)
    input("Enter para volver atras.")

#LISTA DE PRECIOS
# def lista_precios(plata, lista):
#     precioFinal = []
#     precioLista = lista
#     for item in precioLista:
#         metros = item["metros"]*100
#         habitaciones = item["habitaciones"]*500
#         garaje = 0
#         if item["garaje"]:
#             garaje = 1500
#         if item["zona"] == "A":
#             item["precio"] = metros+habitaciones+garaje
#         elif item["zona"] == "B":
#             item["precio"] = (metros+habitaciones+garaje)*1.5
#         elif item["zona"] == "C":
#             item["precio"] = (metros+habitaciones+garaje)*2
#     for item in precioLista:
#         if item["estado"]!="Vendido" and item["precio"] < plata:
#             precioFinal.append(item)
#     for index, item in enumerate(precioFinal):
#         print("Indice: ", index, "item: ", item)
#     input("Enter para continuar")


#LISTA DE PROPIEDADES/INMUEBLES        
propiedades = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]
#MENU DEL INICIO
while True:
    # for indice, inmueble in enumerate(propiedades):
    #     print(f"Indice: {indice}, Inmueble {inmueble}")
    # print()
    menu()
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        añadir_propiedad(propiedades)
    elif opcion == "2":
        editar_propiedad()
    elif opcion == "3":
        eliminar_propiedad(propiedades)
    elif opcion == "4":
        modificar_estado()
    elif opcion == "5":
       ver_lista()
    elif opcion == "6":
        presupuesto = int(input("Inserte su presupuesto: "))
        lista_precios(presupuesto, propiedades)

    elif opcion == "7":
        break
    



