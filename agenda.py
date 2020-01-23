#Diccionario que hace de agenda
dic = {
'Anthony':['Luzquiños', '936962826', 'sluzquinosa@uni.pe']
'Israel': ['temoche', '94535928','israel.temoche.l@uni.pe']
}
def mostrar_contactos ():
    print ('Contactos: ')
    for position, key in enumerate (dic):
        print(position + 1, key, dic[key])

def agregar_contacto (nombre):
    pass
def buscar_contacto(nombre):
    pass
def eliminar_contacto():
    pass
