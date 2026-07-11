# a = int(input('Hey, enter the number: '))

# print(a)

# Exception in python can be handled using a try statement. The code that handles the exception is written in the except clause.

try:
  a = int(input('Hey, enter the number: '))

except ValueError as valE:
  print(valE)

except Exception as e:
  print(e, 'Enter the valid number.')

# When the exception is handled, the code flow continues without program interruption. 

# For example, if a user a string instead of a number.