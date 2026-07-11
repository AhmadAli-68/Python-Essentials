a = int(input('Enter a number: '))
b = int(input('Enter a second number: '))

if b == 0 :
  raise ZeroDivisionError('Hey this program is not meant to divide number by zero')

else:
  print(f'The division of numbers a and b is {a / b}')