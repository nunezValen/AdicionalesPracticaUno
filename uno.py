letra = input("Ingrese una letra: ")
while letra != "TERMINAR":  
    if ((letra >= "a") and (letra <="z")):
       print("Minuscula")
    elif ((letra >= "A") and (letra<="Z")) :
        print("Mayuscula")
    else:
        print("Debe de ingresar una letra")
    
    letra = input("Ingrese una letra: ") 
