def buscar(jugadores):
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
                    for clave in jugadores.kyes():
                        if clave==rut:
                            nombre=jugadores["nombre"]
                            posicion=jugadores["posicion"]
                            print(f"El Nombre del jugador es {nombre} y su Posicion es {posicion}") 
                        a=False               

        except ValueError:
                        print("- El RUT debe contener solo números.")






    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    for clave in jugadores.kyes():
        if clave==rut:
            return (jugadores["nombre","posicion"])