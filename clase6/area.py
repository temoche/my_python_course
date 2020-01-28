# Calcularemos el área de un triángulo usando el método de Herón
import math
print('Por favor, ingrese los lados del triángulo: ')
global a, b, c
while True:
  try:
       a = float(input('El valor del primer lado del triángulo es: '))
  except ValueError:
      print('Por favor , debe ingresar un número')

  try:
      b = float(input('El valor del segundo lado del triángulo es: '))
  except ValueError:
      print('Por favor , debe ingresar un número')

  try:
      c = float(input('El valor del tercer lado del triángulo es: '))
  except ValueError:
      print('Por favor , debe ingresar un número')

  if a+b<c or a+c<b or b+c<a or math.fabs(a-b)>c or math.fabs(a-c)>b or math.fabs(b-c)>a:
    print ('El triángulo no existe.')
  else:  
  p = a + b + c
  area = (p*(p-a)*(p-b)*(p-c))**(0.5)
  print ('El área es: ',area)
  break



    


