import os
class Operasbas():
    #Popiedades de clase
    num1=0
    num2=0
    resp=0
    #Constructor de la clase 
    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    def suma(self):
        self.resp=self.num1+self.num2

    def resta(self):
        self.resp=self.num1-self.num2
    
    def multiplicacion(self):
        self.resp=self.num1*self.num2

    def division(self):
        self.resp=self.num1/self.num2

def main():
    os.system("cls")
    opc=(input('******Bienvenido******\nIngresa el número de acuerdo a la operacion a realizar\n1:Suma\n2:Resta\n3:Multiplicación\n4:Division\n5:Salir\n'))
    while ('5' !=opc):
        num1=int(input('Ingresa el primer número\n'))
        num2=int(input('Ingresa el segundo número\n'))
        obj=Operasbas(num1,num2)
        if (opc=='1'):
            print("SUMA\n")
            obj.suma()
            print(obj.resp)
        elif (opc == '2'):
            print("---RESTA--\n")
            obj.resta()
            print(obj.resp)
        elif (opc == '3'):
            print("---MULTIPLICACIÓN--\n")
            obj.multiplicacion()
            print(obj.resp)
        elif (opc == '4'):
            print("---DIVISIÓN--\n")
            obj.division()
            print(obj.resp)
        elif (opc == '5'):
            print("---HAZ SALIDO--")
        else:
            print("*************La opción ingresada no es correcta, vulve a intentarlo*************")
    
        opc=(input('Ingresa el número de acuerdo a la operacion a realizar\n1:Suma\n2:Resta\n3:Multiplicación\n4:Division\n5:Salir\n'))
###Se determina hasta donde debe de ejecutarse

if __name__=='__main__':
    main()
#Metodos de clase 