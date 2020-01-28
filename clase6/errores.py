while True:

     try:
         number = int(input('Type a number: '))
         print(number)
         break
     except ValueError:
         print('The number you \'ve just typed is not an integer')
     finally:
         print('I\'m being always executed') 
 