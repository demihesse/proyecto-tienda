
print("Tienda de juguetes y animales en peligro de extincion")
input("pulse ENTER para continuar...")
usuario = None
contraseña = None  #VARIABLES IMPORTANTES

# DICCIONARIO: cada producto tiene un nombre (clave) y un precio (valor)
productos = {
    "peluche de tigre": 15,
    "peluche de panda": 12,
    "figura de rinoceronte": 8,
    "libro de animales en peligro": 10
}

# FUNCION: agrupa el código de la tienda para poder llamarlo cuando queramos
def tienda():
    carrito = []     # LISTA vacía donde guardaremos lo que el usuario compre
    total = 0         # ACUMULADOR: aquí sumamos el precio de cada producto

    while True:
        print("\n--- PRODUCTOS DISPONIBLES ---")
        # FOR: recorremos el diccionario para mostrar cada producto con su precio
        for nombre, precio in productos.items():
            print(f"{nombre} - ${precio}")

        print("\nescriba el nombre exacto del producto para comprarlo")
        print("o escriba 'salir' para terminar la compra")
        eleccion = input("")

        if eleccion == "salir":
            break
        elif eleccion in productos:
            carrito.append(eleccion)
            total += productos[eleccion]
            print(f"agregado al carrito. total acumulado: ${total}")
        else:
            print("ese producto no existe, intente de nuevo")

    print("\n--- RESUMEN DE COMPRA ---")
    for producto in carrito:
        print(f"- {producto}")
    print(f"TOTAL A PAGAR: ${total}")
while True:
    #INICIO DEL MENU 
    while True:
        print("seleccione una opción:")
        print("1) Registrarse")
        print("2) Iniciar Sesión")
        print("3) Salir")

        opcion = input("")
        if opcion not in ["1", "2", "3"]:
            print("seleccione una opción válida")
        else:
            break
    if opcion == "1":       #CAPTURA DE DATOS
            while True:
                print("BIENVENIDO! registrese por favor.")
                usuario = input("coloque su usuario: ")
                if usuario == "":
                    print("su usuario es inexistente...")
                elif usuario.isdigit():
                    print("el usuario no puede contener solamente números...")
                elif len(usuario) <= 4:
                    print("usuario demasiado corto")
                else:
                    print(f"su usuario es {usuario}, prosiga...")
                    break   
        
            while True:
                contraseña = input("contraseña:  ")
                if contraseña == "":
                    print("su contraseña es imposible...")

                elif contraseña.isdigit():
                    print("la contraseña no puede contener solamente números...")

                elif contraseña.isalpha():
                    print("la contraseña no debe tener solo letras...")

                elif len(contraseña) <= 6:
                    print("contraseña demasiado corta...")
                else:
                    print("contraseña válida.\n")
                    break       #FIN DE LA CAPTURA DE DATOS
            
    if opcion == "2": #OPCIONES ALTERNATIVAS
        if usuario is None or contraseña is None:
            respuesta= input("usted no se ha registrado aun, desea crear una cuenta? 1)si 2)salir\n")
            if respuesta == "1":
                input("vuelva al menu y registrese...ENTER")
                continue 
            elif respuesta == "2":
             exit()
            #el usuario en caso de tener una cuenta. debe tener la opcion de redirigirse al menu e iniciar sesion....                               
    if opcion =="3":
        exit("adios.")
    
    print("REGISTRO COMPLETADO") #FIN DEL REGISTRO Y OTRAS OPCIONES
    seleccion= input ("USTED YA POSEE UN USUARIO, ¿Desea iniciar sesión? 1)SI 2)volver al menu \n")
    intentos = 3
    if seleccion =="1":
        while intentos > 0:
            uc=input("coloque su usuario:\n")
            cc=input("coloque su contraseña:\n")
            if uc == usuario and cc == contraseña:
                print ("ha iniciado sesión exitosamente.")
                tienda()   # LLAMAMOS a la función de la tienda
                break
            else: 
                intentos -=1
                if intentos > 1: print(f"usuario o contraseña incorrectos. Le quedan {intentos} intentos")
                elif intentos == 1: print(f"le queda 1 intento")
                elif intentos == 0: 
                    exit ("Se ha quedado sin intentos. Adios, no vuelva.")
    if seleccion =="2":
        continue 
    #AHORA EL USUARIO DEBERIA INGRESAR A LA TIENDA USANDO SU USUARIO Y CONTRASEÑA... linea 70
    
        
     

        
   




    
    
    
