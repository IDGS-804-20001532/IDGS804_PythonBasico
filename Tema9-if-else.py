print("Sumar dos números")
num1=int(input("Dame el primer número "))
num2=int(input("Dame el segundo número "))
rest=num1+num2
print("La suma de {0} + {1} = {2}".format(num1,num2,rest))

if num1 > num2:
    print("{} es mayor que {}".format(num1,num2))
else:
    print("{} es mayor que {}".format(num2,num1))

print("**************Nuevo Programa*************")

edad=int(input("Ingresa tu edad "))

if edad>18:
    print("Eres mayor de edad")
elif edad==18:
    print("Tienes 10 años!!!")
else:
    print("No eres mayor de edad")


'''
AND
OR
>,<,<=,!
'''

valor1=200
valor2=2
valor3=1000

if(valor1>1000 and valor2>2) or valor3<200:
    print("resultado")


