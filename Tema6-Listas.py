lista1=["Adrián",1,2,23,True]

print(lista1)

print(lista1[:])
print(lista1[2:4])
print(lista1[:2])
print(lista1[3:])

lista1.append("Adrián")
print(lista1)
lista1.insert(0,"Luis")
print(lista1)
lista1.extend([9,10,11])
print(lista1)
print(lista1.index("Adrián"))
lista1.remove("Adrián")
print(lista1)
lista1.pop()
print(lista1)

