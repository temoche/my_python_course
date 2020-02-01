import math

x = 10
y = 10.0
phrase = 'Hello World!'

print(x)
print(y)
print(phrase)
print(type(x))
print(type(y))
print(type(phrase))

x = 3*5
print('El resultado de 3*5 es:',x)
x = 3/5 #division flotante
print(f'El resultado de 3/5 es: {x}')
x = 6//5 #division entera
print('El resultado de 6//5 es:',x)
x = 10 % 7 #residuo
print('El resultado de 10%7 es:',x)
x = 10**3
print('El resultado de 10**3 es:',x)
x = 81**(0.5) #de esta manera se obtiene el mismo resultado que el obtenido mediante sqrt
print (x)
x = math.sqrt(49)
print(x)

radio = float(input('Ingrese el radio del círculo: '))
area = round(math.pi*radio**2, 15)
print (f'El area del círculo es: {area}')