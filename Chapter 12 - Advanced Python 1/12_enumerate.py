list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# index = 0
# for item in list:
#   print(f'The item number at index {index} is {item}')
#   index += 1

#? this can be simplified using the enumerate function.

for index, item in enumerate(list):
  print(f'The item number at index {index} is {item}')