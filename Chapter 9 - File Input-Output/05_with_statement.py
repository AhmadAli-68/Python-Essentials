f = open('file.txt')

print(f.read())
f.close()

#* The same can be written using with statement like below:

with open('file.txt') as file:
  print(file.read())

#? with that, we won't have close the file explicitly.