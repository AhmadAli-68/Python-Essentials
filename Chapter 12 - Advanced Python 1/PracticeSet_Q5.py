num = int(input('Enter the number for that you want to store the table in the list: '))

table = [num * i for i in range(1, 11)]
with open('tables.txt', 'a') as file:
  file.write(f'Table of {num} is: {str(table)} \n')