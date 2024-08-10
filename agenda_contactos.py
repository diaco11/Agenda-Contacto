#AGENDA DE CONTACTOS

def mostrar_contactos():
    print("\nAGENDA CONTACTOS")
    print("1.Agregar Nuevo Contacto")
    print("2.Eliminar Contacto Existente")
    print("3.Buscar Conctacto")
    print("4.Lista de Contacto")
    print("5.Salir del programa")
    print()


def agregar_contacto(agenda:dict):
    nombre = input("Ingrese su nombre: ")    
    telefono = input("Ingrese su telefono: ")  
    email = input("Ingrese su email: ")  
    agenda[nombre] = {"telefono":telefono, "email":email}


def eliminar_contacto(agenda:dict):
    nombre = input("ingrese nombre: ")
    if nombre in agenda:
        del agenda[nombre]
        print("El contacto {nombre} se borro exitosamente.\n")
    else:
        print("El nombre ingresado no se encuentra!!\n")  


def buscar_contacto(agenda:dict):
    nombre = input("ingrese nombre: ")
    if nombre in agenda:
        print(f"Nombre = {nombre}") 
        print(f"Telefono = {agenda[nombre]["telefono"]}")
        print(f"Email = {agenda[nombre]["email"]}\n")
    else:
        print(f"No se encuentra el contacto {nombre}\n")            


def lista_contacto(agenda:dict):
    if agenda:
        print("\nLISTA DE CONTACTOS:")
        for name, info in agenda.items():
            print(f"Nombre: {name}")
            print(f"Telefono: {info["telefono"]}")
            print(f"Email: {info["email"]}")
            print("-" * 20,"\n")
    else:
        print("La Agenda se encuentra vacia.\n")        



def agenda_contactos():
    agenda = {}

    while True:
        mostrar_contactos()
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            lista_contacto(agenda)
        elif opcion == "5":
            print("Saliendo del programa!!")
            break


agenda_contactos()