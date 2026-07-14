juegos = [
]
inventario = [

]

def agregar_juego():
    codigo = input("ingrese el codigo del juego >> ")
    Titulo = input("Nombre del videojuego >> ")
    plataforma = input("plataforma en que se juega >> ")
    genero = input("genero del juego >> ")
    clasificacion = input("clasificacion de edad del juego >> ")
    multiplayer = input("indica si el juego permite modo multijugador  >> ")
    editor = input("que empresa edito el juego >> ")
    precio = int(input("ingrese el preico del juego >> "))
    stock = int(input("ingrese el stock del juego disponible >> "))

    juego_agregado = {"Codigo": codigo, "Titulo": Titulo, "Plataforma": plataforma, "Genero": genero, "Clasificacion": clasificacion, "Multiplayer": multiplayer, "Editor": editor, "Precio": precio, "Stock": stock}

    juegos.append(juego_agregado)
    inventario.append({"Precio": precio, "Stock": stock})
    print("juego agregado con exito")
    print(juegos)
    print("--------------------------------")
    return juegos

def busqueda_precio():
    print("------------------------------------------")
    precios = [2000, 50000]
    precio = int(input("que precio tiene su juego >> "))
    if precio in precios:
     for J in inventario:
        if J["Precio"] == precio:
            print(J)
            print("--------------------------------")

def stock_plataforma():
    print("----------------------------------------------")
    plataforma_buscar = input("que plataforma busca >> ")
    for E in juegos:
        if E["Plataforma"] == plataforma_buscar:
            print(E)
    stock = int(input("cuanto stock tiene su juego >> "))
    for O in juegos:
        if O["Stock"] == stock:
            print(O)
            print("-----------------------------------------------")

def actualizar_precio():
    print("------------------------------------------------")
    codigo_abuscar = input("que juego busca >> ")
    for i in juegos:
        if i["Codigo"] == codigo_abuscar:
            nuevo_precio = int(input("que nuevo precio desea ponerle al juego >> "))
            i["Precio"] = nuevo_precio  # Actualizar el precio en el diccionario del juego
            print("-----------------------------------------------------------------")
    return

def eliminar_juego():
    codigo_abuscar = input("que juego busca >> ")
    for Y in juegos:
        if Y["Codigo"] == codigo_abuscar:
            print("juego eliminado con exito")
            juegos.remove(Y)
            print(juegos)


def leer_op():
    opciones_validas = ["1", "2", "3", "4", "5", "6"]
    while True:
        print("-------MENU PRINCIPAL-------")
        print("1.- Stock por plataforma")
        print("2.- busqueda de juegos por rango de precio")
        print("3.- Actualizar precio de juego")
        print("4.- agregar juego")
        print("5.- eliminar juego")
        print("6.- salir")
        print("----------------------------")
        opcion = input("que opcion va a elegir >> ")
        if opcion in opciones_validas:
            return opcion
        
while True:
        opcion = leer_op()
        if opcion == "1":
            stock_plataforma()
        elif opcion == "2":
            busqueda_precio()
        elif opcion == "3":
            actualizar_precio()
        elif opcion == "4":
            agregar_juego()
        elif opcion == "5":
            eliminar_juego()
        elif opcion == "6":
            print("gracias por usar ")
            break
        else: 
            print("opcion no valida, intente de nuevo")
        
        
