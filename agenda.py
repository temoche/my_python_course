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
if(opcion == 0):
    break
elif 




 #actividad.
 # Generar un menú con las opciones antes programadas y que termine al ingresar "0".                

