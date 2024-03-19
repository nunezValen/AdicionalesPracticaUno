cadena=input("Ingrese una cadena de caracteres ")
total=0
for car in cadena:
    if ((car=="a") or (car=="A")):
        total=total+1
print(f"La cadena tenia un total de {total} letras \"a\"")

nombre="valen"
apellido="nuñez"
print(f"Su nombre es {nombre + apellido}")