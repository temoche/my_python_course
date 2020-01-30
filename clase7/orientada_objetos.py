#Clase
#   Son abstracciones de las cosas de la vida cotidiana
#   Moldes o plantillas para crear objetos

#Objeto
#   Un ejemplo de una clase en particular 
#   Una instancia de clase

class Person():

    #CONSTRUCTOR
     def __init__(self, name,last_name, age):
         #ATRIBUTES
         self.name = name
         self.last_name = last_name
         self.age = age

     #Method    
     def greet(self):
         return 'Hi!, my name is ' + self.name + ' ' + self.last_name + ', I\'m  ' + str(self.age) + ' years old.'    



person_1 = Person('Anthony','Luzquiños', 15)
person_2 = Person('Ruben','Ricapa',23)

print(person_1.greet())
print(person_2.greet())


