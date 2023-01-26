def tem1():
    print("¡Hola desde my_module.py!")

def tem2():
    print("!Adios desde my_module.py!")

def main():
    print("¡Hola desde main!")
    tem1()
    tem2()

###Se determina hasta donde debe de ejecutarse
if __name__=='__main__':
    main()