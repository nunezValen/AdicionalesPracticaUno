list=[]
x=int(input("Ingrese un numero a la lista "))
while x != 0:
    list.append(x)
    x=int(input("Ingrese otro numero a la lista "))
for elem in list:
    if elem>0:
        print(elem)
    else:
        break