#Diccionario que hace de agenda
dic = {
'Anthony':['Luzquiños', '936962826', 'sluzquinosa@uni.pe'],
'Israel' :['temoche', '94535928','israel.temoche.l@uni.pe']
}
def mostrar_contactos ():
    print ('Contactos: ')
    for position, key in enumerate (dic):
        print(position + 1, key, dic[key])
    print()

def agregar_contacto (nombre):
    apellido = str(input('Ingrese el apellido del contacto: \n'))
    numero = int(input('Ingrese el número de celular del contacto: \n'))
    correo = str(input('Ingrese el correo electrónico del nuevo contacto:\n'))
    dic[nombre] = [apellido,numero,correo]
    mostrar_contactos()
    
def buscar_contacto(nombre):
    if nombre in dic:
        print ('Contacto encontrado: ')
        print(nombre, dic[nombre])
    else:
        print('No existe el contacto')
    print()
def eliminar_contacto(nombre):
    dic.pop(nombre)
    mostrar_contactos()

while True:
     print ('Por favor seleccione una opción \n 1) Ver contactos \n 2) Agregar contactos \n 3) Buscar contactos \n 4) Eliminar contactos \n Presione 0 para salir')
     opcion = int(input())
 
     if (opcion == 0):
         break
     elif (opcion == 1 ):                
         mostrar_contactos()
     elif (opcion == 2):
         name = str(input('Ingrese el nombre del nuevo contacto: \n'))
         agregar_contacto(name)
     elif (opcion == 3):
         name = str(input('Ingrese el nombre del contacto que desea buscar: \n'))
         buscar_contacto(name)
     elif (opcion == 4):
         name = str(input('Ingrese el nombre del contacto que usted desee eliminar: \n'))
         if name in dic:
             eliminar_contacto(name) 
         else: print('El contacto ingresado no existe. \n Por favor, intente de nuevo. \n')             

      




 #actividad.
 # Generar un menú con las opciones antes programadas y que termine al ingresar "0".  