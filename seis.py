list=[1,2,3,4,5,6,7,8]
listPar=[]
listImp=[]
for x in list:
    if x% 2 ==0:
        listPar.append(x)
    else:
        listImp.append(x)
print(f"Lista de pares: {listPar}")
print(f"Lista de impares: {listImp}")