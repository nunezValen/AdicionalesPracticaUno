list=[]
cadena=""
x=int(input("Ingrese un numero "))
while x !=0:
    list.append(x)
    x=int(input("Ingrese un numero "))
for elem in list:
    if elem % 3==0:
        continue
    else:
        str(elem)
        cadena=f"{cadena}{elem}-"
print(cadena)