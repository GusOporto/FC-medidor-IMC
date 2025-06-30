import MisFunciones

jugadores={"170487893":{"nombre":"GUS","peso":80,"estatura":1.70,"posicion":"4"},
           }


while True:
    print("Menú")
    print("1. Registrar Jugadores")
    print("2. Buscar Jugador por RUT")
    print("3. Mostrar estado Nutricional")
    print("4. Lista de equipo completo")
    print("5. Contar jugadores por Posicion")
    print("6. Salir del sistema")

    opc=int(input("\n- Elija una opcion del Menú: "))

    if opc==1:
        print("-- Registrar Jugadores --")
        a=True
        while a==True:
            try:
                print("* Si el RUT termina en K, reemplacela por un 0 *")
                rut=input("Ingrese el RUT del jugador (sin puntos ni guión): ")

                if len(rut)<9:
                    print("- El RUT debe tener 9 digitos.")
                else:                
                    for letra in rut:
                        if letra.isalpha():
                            print("- El RUT debe contener solo números.")
                            a=True
                            break
                    else:                                                   
                        for clave in jugadores.keys():
                            if clave==rut:
                                print("- El RUT ya está registrado")
                                a=True     
                                break  
                            else:
                                a=False                  
                            
            except ValueError:
                print("- El RUT debe contener solo números.")
                                                  

        nombre=input("\nIngrese el Nombre del jugador: ")
        
        while True:
            try:
                peso=int(input("\nIngrese el Peso del jugadro en Kilogramos: "))
                if peso<=0:
                    print("- El Peso no puede ser menor a 0.")                
                else:
                    break
            except ValueError:
                print("- El Peso debe contener solo números.")
        
        while True:
            try:
                estatura=float(input("\nIngrese la Estatura del jugador en Metros: "))
                if estatura<=0:
                    print("- La Estatura no puede ser menor a 0.")
                else:
                    break
            except ValueError:
                print("- La Estatura debe contener solo numeros.")

        while True:
            try:
                print("1- Arquero\n2- Defensa\n3- Mecio Campo\n4- Delantero")

                posicion=int(input("\nIngrese la Posicion del jugador: "))

                if posicion<1 or posicion>4:
                    print("- Las Posiciones disponebles son de 1 a 4")
                    print("1- Arquero\n2- Defensa\n3- Mecio Campo\n4- Delantero")
                elif posicion.isalpha():
                    raise ValueError
                else:
                    if posicion==1:
                        posicion="Arquero"
                    elif posicion==2:
                        posicion="Delantero"
                    elif posicion==3:
                        posicion="Defensa"
                    elif posicion==4:
                        posicion="Medio Campo"
                    break                
                    
            except ValueError:
                print("- La Posicion debe ser en en números.")
                print("1- Arquero\n2- Defensa\n3- Mecio Campo\n4- Delantero")

        jugadores[rut]={"nombre":nombre,
                        "peso":peso,
                        "estatura":estatura,
                        "posicion":posicion
                        }

    elif opc==2:
        print("-- Buscar Jugador por RUT --")
        jugadores=jugadores{}
        MisFunciones.buscar(jugadores)
        



    