#Diccionario que hace de agenda
dic = {
'Anthony':['Luzquiños', '936962826', 'sluzquinosa@uni.pe'],
'Israel' :['temoche', '94535928','israel.temoche.l@uni.pe']
}
def mostrar_contactos ():
    print ('Contactos: ')
    for position, key in enumerate (dic):
        print(position + 1, key, dic[key])

def agregar_contacto (nombre):
    dic ['nombre'] = 'apellido'
    print (dic)
    
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

print ('Por favor seleccione una opción \n 1) Ver contactos \n 2) Agregar contactos \n 3) Buscar contactos \n 4) Eliminar contactos \n Presione 0 para salir')
opcion = int(input())


validator = True
while validator:
     while validator:
              if(opcion == 0):
                 validator = False
              elif (opcion == 1):
                mostrar_contactos()
                break
         
              elif (opcion == 2):
                 agregar_contacto()
                 break
         
              elif (opcion == 3):
                 buscar_contacto()  
                 break 
         
              elif (opcion == 4):
                 eliminar_contacto()
                 break 
              else:
                 print ('El número ingresado no es una opción válida. \n Por favor, intente de nuevo')    
                    
     else:
          break      




 #actividad.
 # Generar un menú con las opciones antes programadas y que termine al ingresar "0".  