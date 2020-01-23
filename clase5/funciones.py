#Funciones

variable = 27
print (variable)


def saludar():
    print ('hola, mundo')
saludar()   
def salir():
    global variable 
    variable += 2
    print (variable)
    print('Nos vemos \n miau')
salir()    